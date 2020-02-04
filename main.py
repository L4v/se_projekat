from parser import Parser
from trie import Trie
from graph import Graph
import os

def main():
    parser = Parser()
    graph = Graph()
    start = input('Unesite root dir: ')
    for root, dirs, files in os.walk(start):
        path = root
        for file in files:
            if file[-5:] == '.html':
                print(path + os.sep + file)

if __name__ == "__main__":
    main()


