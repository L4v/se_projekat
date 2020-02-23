# main.py
from utils.parser import Parser
from datatypes.trie import Trie
from ui.unos import unos_upita
from datatypes.graph.graph import Graph
from datatypes.graph.vertex import Vertex
from ui.search_display import SearchDisplay
from utils.ranker import rank_pages
from utils.timsort import timsort
from ui.colors import Colors as col
from ui.custom_print import err

import sys
import os


# NOTE(Jovan): Ukradeno od Vladimir Ignatyev:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress_bar(count, total, suffix=''):
    bar_len = 60
    total = total if total > 0 else 1
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


def menu_header(text, max_len=51, padding=3):
    decor_len = (max_len - len(text) - 2 * padding)//2
    decor_len = 0 if decor_len <= 0 else decor_len
    print('='*decor_len + ' '*padding
          + col.bold + text + col.rst
          + ' '*padding + '='*decor_len)


# NOTE(Jovan): Glavni meni
def menu():
    options = [
            'Odaberite opciju:',
            '\t1.Pretraga reci',
            '\t0.Izlaz'
            ]
    print('\n'.join(options))
    while True:
        try:
            option = int(input('>'))
            break
        except Exception:
            err('Unos mora biti broj')
    return option


def load_graph(graph):
    parser = Parser()
    while True:
        start = input('Unesite root dir: ')
        if os.path.isdir(start):
            for fname in os.listdir(start):
                curr = os.path.join(start, fname)
                if os.path.isdir(curr) or curr.endswith('.html'):
                    break
            else:
                err('Nije validna putanja')
            break
        else:
            err('Nije validna putanja')
    current = 0
    for root, dirs, files in os.walk(start):
        for file in files:
            current = loading_rotation(current, 'Ucitavanje grafa...')
            if file[-5:] == '.html':
                path = root + os.path.sep + file
                path_root = os.path.abspath(os.path.dirname(path))
                filepath = path_root + os.path.sep + file
                links, words = parser.parse(path)
                # NOTE(Jovan): Informacije o stranici pretvaraju se u vertex
                vertex = Vertex(filepath, words, links)
                graph.add_vertex(vertex)
    graph.gen_backlinks()
    loading_rotation(current, col.bold+col.green+'Ucitavanje zavrseno'+col.rst)
    print()
    return graph.vertex_count()


def load_trie(graph, trie):
    # dodavanje reci u trie
    total = graph.vertex_count()
    count = 0
    for vertex in graph.vertices():
        progress_bar(count, total, 'Ucitavam stablo...')
        for word in vertex.words:
            trie.add(word.lower(), vertex.path)
        count += 1
    count = total
    progress_bar(count, total, col.bold+col.green+'Stablo ucitano'+col.rst)
    print()


def page_menu(search_display):
    options = [
            'Odaberite opciju:',
            '\t1. Prikazi odredjenu stranu',
            '\t2. Promeni broj rezultata po strani',
            '\t3. Sledeca',
            '\t4. Prethodna',
            '\t0. Nazad',
            ]
    # NOTE(Jovan): Pocetna strana je 1.
    page_num = 1
    while True:
        search_display.display(page_num)
        menu_header('MENI PRIKAZA')
        print('\n'.join(options))
        while True:
            try:
                option = int(input('>'))
                break
            except Exception:
                err('Unos mora biti broj')

        # NOTE(Jovan): Unos strane
        if option == 1:
            try:
                page_num = int(input('Broj strane: '))
            except Exception:
                err('Unos mora biti broj')

        # NOTE(Jovan): Promena broja rezultata po strani
        if option == 2:
            try:
                num_results = int(input('Broj rezultata: '))
                page_num = 1
            except Exception:
                err('Unos mora biti broj')
            search_display.set_count(num_results)

        # NOTE(Jovan): Sledeca strana
        if option == 3:
            max_num = search_display.page_count
            page_num = page_num + 1 if page_num < max_num else max_num

        # NOTE(Jovan): Prethodna strana
        if option == 4:
            page_num = page_num - 1 if page_num > 1 else 1

        # NOTE(Jovan): Izlaz
        if option == 0:
            break


def main():
    # NOTE(Jovan): Glavni loop
    graph = Graph()
    trie = Trie()
    while True:
        count = load_graph(graph)
        if count > 0:
            break
        else:
            err('Nije pronadjena nijedna .html stranica')

    load_trie(graph, trie)
    while True:
        menu_header('GLAVNI MENI')
        option = menu()

        if option == 1:
            results = unos_upita(trie, graph).values
            ranked = rank_pages(graph, results).values
            timsort(ranked)
            search_result = SearchDisplay(ranked)
            page_menu(search_result)
        elif option == 0:
            break
        else:
            err('Nepoznata opcija')


if __name__ == "__main__":
    main()
