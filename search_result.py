class SearchDisplay:

    def __init__(self, results, count=None):
        self._results = results
        self._pages = []
        self._count = 1 if count is None else count

    def set_count(self, count):
        if count >= 1:
            self._count = count
        else:
            self._count = 1

    def _paginate(self):
        self._pages.append(
                self._results[i:i+self._count]
                for i in range(0, len(self._results), self._count)
        )

    def display(self, page_num):
        if page_num >= len(self._pages):
            print('Strana ne postoji')
            return
        self._paginate()
        print(f'#### STRANA {page_num} ####')
        for page in self._pages[page_num]:
            print(page)
