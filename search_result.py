class SearchDisplay:

    def __init__(self, results, count=None):
        self._results = results
        self._pages = []
        self._count = 1 if count is None or count < 1 else count

    def set_count(self, count):
        self._count = 1 if count <= 1 else count

    def _paginate(self):
        self._pages = []
        for res in self._results:
            tmp = []
            for i in range(0, self._count):
                tmp.append(res)
            self._pages.append(tmp)
        self._pages = [self._results[i:i+self._count]
                       for i in range(0, len(self._results), self._count)]

    def display(self, page_num):
        self._paginate()
        if page_num >= len(self._pages):
            print('Strana ne postoji')
            return
        print(f'#### STRANA {page_num} ####')
        for page in self._pages[page_num]:
            print(page)
