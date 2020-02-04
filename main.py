from parser import Parser
from trie import Trie
from unos_upita import unos


def main():
    parser = Parser()
    str = parser.parse('temp/python-2.7.7-docs-html/copyright.html')
    trie = Trie()
    for rec in str[1]:
        trie.add(rec)

    print(trie.find('Python'))

    unos()

if __name__ == "__main__":
    main()


