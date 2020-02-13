class Result:
    __slots__ = ['_page', '_count']

    def __init__(self, page, count=None):
        self._page = page
        self._count = 1 if count is None else count

    def __iadd__(self, other):
        self._count += other

    def __eq__(self, other):
        return isinstance(other, Result) and self._page == other._page and self._count == other._count

    def get_count(self):
        return self._count

    def get_page(self):
        return self._page
