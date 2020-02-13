class Result:
    __slots__ = ['_path', '_count']

    def __init__(self, path, count=None):
        self._path = path
        self._count = 1 if count is None else count

    def __iadd__(self, other):
        self._count += other
        return self

    def __eq__(self, other):
        return isinstance(other, Result) and self._path == other._path

    def get_count(self):
        return self._count

    def get_path(self):
        return self._path
    
    def __str__(self):
        return self._path + ': ' + str(self._count)
