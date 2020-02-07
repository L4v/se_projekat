from parser import Parser
from trie import Trie
from unos_upita import unos
from graph import Graph
from page import Page
import sys
import os


# NOTE(Jovan): Ukradeno od Vladimir Ignatyev:
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress_bar(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + ' ' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()


def menu():
    options = [
            'Odaberite opciju:',
            '\t1.Odabir root direktorijuma ',
            '\t0.Izlaz'
            ]
    for o in options:
        print(o)
    option = int(input('>'))
    return option


def load_graph(graph):
    parser = Parser()
    start = input('Unesite root dir: ')
    # TODO(Jovan): Generisanje ID-a za svaki page kako se ne bi
    # moralo ucitavati vise puta?
    print('Ucitavanje grafa...')
    for root, dirs, files in os.walk(start):
        for file in files:
            if file[-5:] == '.html':
                path = root + os.path.sep + file
                path_root = os.path.abspath(os.path.dirname(path))
                # TODO(Jovan): Je l potrebno?
                # print(f'Ucitavam: {path}')
                links, words = parser.parse(path)
                page = Page(path_root + os.path.sep + file, words, links)
                graph.add_vertex(page)

    print('Ucitavanje zavrseno\n')
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
    print('Veze stvorene')
    print('Graf:', graph)


def load_trie(graph, trie):
    # dodavanje reci u trie
    total = graph.vertex_count()
    count = 0
    for page in graph.vertices():
        progress_bar(count, total, 'Ucitavam stablo...')
        for word in page.words:
            trie.add(word, page.path)
        count += 1


def main():
    # NOTE(Jovan): Glavni loop
    graph = Graph()
    trie = Trie()
    while True:
        option = menu()
        if option == 1:
            load_graph(graph)
            load_trie(graph, trie)

        if option == 0:
            break

    unos(trie, graph)


if __name__ == "__main__":
    main()
