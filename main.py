from parser import Parser
from trie import Trie
from unos import unos_upita
from graph.graph import Graph
from graph.vertex import Vertex
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
    print('\n'.join(options))
    while True:
        try:
            option = int(input('>'))
            break
        except Exception:
            print('Unos mora biti broj!')
    return option


def load_graph(graph):
    parser = Parser()
    while True:
        start = input('Unesite root dir: ')
        if os.path.isdir(start):
            for fname in os.listdir(start):
                if os.path.isdir(os.path.join(start, fname):
                        break
            else:
                
            break
        else:
            print('Nije validna putanja')
    # TODO(Jovan): Generisanje ID-a za svaki page kako se ne bi
    # moralo ucitavati vise puta?
    current = 0
    for root, dirs, files in os.walk(start):
        for file in files:
            current = loading_rotation(current, 'Ucitavanje grafa...')
            if file[-5:] == '.html':
                path = root + os.path.sep + file
                path_root = os.path.abspath(os.path.dirname(path))
                links, words = parser.parse(path)
                # NOTE(Jovan): Informacije o stranici pretvaraju se u vertex
                vertex = Vertex(path_root + os.path.sep + file, words, links)
                graph.add_vertex(vertex)
    loading_rotation(current, 'Ucitavanje zavrseno')
    print()


def load_trie(graph, trie):
    # dodavanje reci u trie
    total = graph.vertex_count()
    count = 0
    for vertex in graph.vertices():
        progress_bar(count, total, 'Ucitavam stablo...')
        for word in vertex.get_words():
            trie.add(word, vertex.get_path())
        count += 1
    count = total
    progress_bar(count, total, 'Stablo ucitano')
    print()


def page_menu(search_display):
    options = [
            'Odaberite opciju:',
            '\t1. Prikazi odredjenu stranu',
            '\t2. Promeni broj rezultata po strani',
            '\t0. Nazad',
            ]
    page_num = 0
    while True:
        search_display.display(page_num)
        print('*** PAGE MENU ***')
        print('\n'.join(options))
        while True:
            try:
                option = int(input('>'))
                break
            except Exception:
                print('Unos mora biti broj!')

        if option == 1:
            try:
                page_num = int(input('Broj strane: '))
            except Exception:
                print('Unos mora biti broj!')

        if option == 2:
            try:
                num_results = int(input('Broj rezultata: '))
            except Exception:
                print('Unos mora biti broj!')
            search_display.set_count(num_results)

        if option == 0:
            break


# TODO IMPORTANT(Jovan): IMPLEMENTIRATI BOLJU VARIJANTU OD os.walk()
def main():
    # NOTE(Jovan): Glavni loop
    is_loaded = False
    graph = Graph()
    trie = Trie()
    while True:
        print('*** GLAVNI MENI ***')
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
                # TODO(Jovan): Pagerank ovde na results i onda prikaz
                # TODO(Jovan): Isto ucinit set iterable?
                search_result = SearchDisplay(results._values)
                page_menu(search_result)

            else:
                print('Potrebno je prvo odabrati root direktorijum')
        elif option == 0:
            break
        else:
            print('Nepoznata opcija')


if __name__ == "__main__":
    main()
