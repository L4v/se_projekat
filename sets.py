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


class Set():
    def __init__(self, values=None):
        self._values = list(dict.fromkeys(values)) if values is not None else []

    def add(self, item):
        if item not in self._values:
            self._values.append(item)

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return SetIterator(self)

    # TODO(Jovan): Dodati throw???
    def __getitem__(self, index):
        if index >= 0 and index < len(self._values):
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
