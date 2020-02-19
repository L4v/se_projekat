# sets.py
class SetIterator:
    def __init__(self, set_obj):
        self._set = set_obj
        self._index = 0

    def __next__(self):
        if self._index < len(self._set._values):
            result = self._set._values[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


# TODO(Jovan): Bolja provera duplikata?
class Set():
    def __init__(self, values=None):
        if values is None:
            values = []
        self._values = values
        self._remove_duplicates()

    def add(self, item):
        if item not in self._values:
            self._values.append(item)

    def _remove_duplicates(self):
        self._values = list(dict.fromkeys(self._values))

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return SetIterator(self)

    def __setitem__(self, index, value):
        if index >= 0 and index < len(self._values):
            self._values[index] = value
            self._remove_duplicates()

    # TODO(Jovan): Dodati throw???
    def __getitem__(self, index):
        return self._values[index]

    # NOTE(Jovan): AND '*'
    def __mul__(self, other):
        ret = Set()
        for i in self._values:
            if i in other:
                ret.add(i)
        return ret

    # NOTE(Jovan): OR '+'
    def __add__(self, other):
        ret = Set(self._values)
        for i in other:
            ret.add(i)
        return ret

    # NOTE(Jovan): NOT '-'
    def __sub__(self, other):
        ret = Set()
        for i in self._values:
            if i not in other:
                ret.add(i)
        return ret

    def __str__(self):
        return str('(' + ', '.join(map(str, self._values)) + ')')
