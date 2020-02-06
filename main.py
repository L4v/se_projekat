from parser import Parser
from trie import Trie
from unos_upita import unos
from graph import Graph
from page import Page
import os


def main():
    parser = Parser()
    graph = Graph()
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
               page = Page(path_root+os.path.sep+file, words, links)
               print(links)
               graph.add_vertex(page)
        
    print('Ucitavanje zavrseno\nStvaram veze...')
    # NOTE(Jovan): Stvaranje veza
    # NOTE(Jovan): path je key u pages dict
    for page in graph.vertices(): 
        links = page.links
        # NOTE(Jovan): full_path sluzi za dobavljanje pune putanje stranice
        # sa kojom stvaramo vezu
        full_path = page.path.rsplit(os.path.sep, 1)[0]
        for l in links:
            # TODO IMPORTANT(Jovan): VRACA FULL PATH, URADITI NA OSNOVU TOGA
            graph.add_edge(page, graph.get_vertex(l))
            print(f'Adding edge v: {page.path} u:{l}')
    print('Veze stvorene')
    print('Graf:', graph)

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


