from parser import Parser
from trie import Trie
from unos import unos_upita
from graph import Graph
from page import Page
from search_result import SearchDisplay

import sys
import os


# NOTE(Jovan): Ukradeno od Vladimir Ignatyev:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress_bar(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + ' ' * (bar_len - filled_len)
    # NOTE(Jovan): Radice samo ako se pokrene preko terminala, kao sto je
    # Linus Torvalds i namenuo
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()


# NOTE(Jovan): Kada se vrsi ucitavanje nepoznate duzine
def loading_rotation(current, string=''):
    symbols = ['\\', '|', '/', '-', '\\', '|', '/', '-']
    sys.stdout.write('%s [%s]\r' % (string, symbols[current]))
    return (current + 1) % len(symbols)


def menu():
    options = [
            'Odaberite opciju:',
            '\t1.Odabir root direktorijuma ',
            '\t2.Pretraga reci',
            '\t0.Izlaz'
            ]
    for o in options:
        print(o)
    while True:
        try:
            option = int(input('>'))
            break
        except Exception:
            print('Unos mora biti broj!')
    return option


def load_graph(graph):
    parser = Parser()
    start = input('Unesite root dir: ')
    # TODO(Jovan): Generisanje ID-a za svaki page kako se ne bi
    # moralo ucitavati vise puta?
    current = 0
    for root, dirs, files in os.walk(start):
        for file in files:
            current = loading_rotation(current, 'Ucitavanje grafa...')
            if file[-5:] == '.html':
                path = root + os.path.sep + file
                path_root = os.path.abspath(os.path.dirname(path))
                # TODO(Jovan): Je l potrebno?
                # print(f'Ucitavam: {path}')
                links, words = parser.parse(path)
                page = Page(path_root + os.path.sep + file, words, links)
                graph.add_vertex(page)
    loading_rotation(current, 'Ucitavanje zavrseno')
    print()

    # NOTE(Jovan): Stvaranje veza
    total = graph.vertex_count()
    count = 0
    for page in graph.vertices():
        progress_bar(count, total, 'Stvaram veze...')
        links = page.links
        for l in links:
            u = graph.get_vertex(l)
            # TODO(Jovan): get_vertex ce puci ako je u iznad root dir sto je
            # mozda i normalno?
            graph.add_edge(page, u)
        count += 1
    progress_bar(count, total, 'Veze stvorene')
    print()


def load_trie(graph, trie):
    # dodavanje reci u trie
    total = graph.vertex_count()
    count = 0
    for page in graph.vertices():
        progress_bar(count, total, 'Ucitavam stablo...')
        for word in page.words:
            trie.add(word, page.path)
        count += 1
    count = total
    progress_bar(count, total, 'Stablo ucitano')
    print()


# TODO IMPORTANT(Jovan): IMPLEMENTIRATI BOLJU VARIJANTU OD os.walk()
def main():
    # NOTE(Jovan): Glavni loop
    is_loaded = False
    graph = Graph()
    trie = Trie()
    while True:
        if not is_loaded:
            print('*** ROOT NIJE OTVOREN ***')
        option = menu()
        if option == 1:
            load_graph(graph)
            load_trie(graph, trie)
            is_loaded = True

        elif option == 2:
            if is_loaded:
                results = unos_upita(trie)

                search_result = SearchDisplay(results)
                search_result.display(0)

            else:
                print('Potrebno je prvo odabrati root direktorijum')
        elif option == 0:
            break
        else:
            print('Nepoznata opcija')


if __name__ == "__main__":
    main()
