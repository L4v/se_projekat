class Result:
    __slots__ = ['_path', '_count']

    def __init__(self, path, count=None):
        self._path = path
        self._count = 1 if count is None else count

    @property
    def path(self):
        return self._path

    @property
    def count(self):
        return self._count

    def inc(self, amount):
        self._count += amount

    def __iadd__(self, other):
        return Result(self._path, self._count + other._count)

    def __eq__(self, other):
        return isinstance(other, Result) and self._path == other._path

    def __hash__(self):
        return hash(self._path)

    def __str__(self):
        return self._path + ': ' + str(self._count)
