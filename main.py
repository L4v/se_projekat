from parser import Parser
from trie import Trie
from unos_upita import unos
from graph import Graph
from page import Page
import os

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
        for root, dirs, files in os.walk(start):
            for file in files:
                if file[-5:] == '.html':
                   path = root + os.path.sep + file
                   path_root = os.path.abspath(os.path.dirname(path))
                   print(f'Ucitavam: {path}')
                   links, words = parser.parse(path)
                   page = Page(path_root + os.path.sep + file, words, links)
                   graph.add_vertex(page)
            
        print('Ucitavanje zavrseno\nStvaram veze...')
        # NOTE(Jovan): Stvaranje veza
        for page in graph.vertices(): 
            links = page.links
            # NOTE(Jovan): full_path sluzi za dobavljanje pune putanje stranice
            # sa kojom stvaramo vezu
            full_path = page.path.rsplit(os.path.sep, 1)[0]
            for l in links:
                u = graph.get_vertex(l)
                # TODO(Jovan): get_vertex ce puci ako je u iznad root dir sto je mozda i normalno?
                graph.add_edge(page, u) 
                print(f'Adding edge v: {page.path} u:{l}')
        print('Veze stvorene')
        print('Graf:', graph)


def main():
    # NOTE(Jovan): Glavni loop
    graph = Graph()
    while True:
        option = menu()
        if option == 1:
            load_graph(graph)

        if option == 0:
            break

    # dodavanje reci u trie
    trie = Trie()
    for page in graph.vertices():
        for word in page.words:
            trie.add(word)

    print(trie.find('Python'))
    print(trie.find('Kris'))

    unos(trie, graph)

if __name__ == "__main__":
    main()


