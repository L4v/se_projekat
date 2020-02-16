class SearchDisplay:

    def __init__(self, results, count=None):
        self._results = results
        self._pages = []
        self._count = 1 if count is None or count < 1 else count

    def set_count(self, count):
        if count <= 1:
            self._count = 1
        elif count >= len(self._results):
            self._count = len(self._results)
        else:
            self._count = count

    def _paginate(self):
        self._pages = [self._results[i:i+self._count]
                       for i in range(0, len(self._results), self._count)]

    def display(self, page_num):
        self._paginate()
        page_max = len(self._pages)
        if page_num > page_max or page_num <= 0:
            print(f'Strana {page_num} ne postoji!')
            return
        print(f'#### STRANA {page_num}/{page_max} ####\n')
        page_len = len(self._pages[0])
        for i, page in enumerate(self._pages[page_num-1],
                                 start=(1 + (page_num-1) * page_len)):
            print(f'{i} - {page}')
        print(f'\n#### KRAJ STRANE {page_num}/{page_max} ####')
