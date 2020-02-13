class Set():
    def __init__(self, values=None):
        self._values = values if values is not None else []

    # TODO(Jovan): Dodati throw???
    def __getitem__(self, index):
        if index >= 0 and index < len(self._values):
            return self._values[index]

    def add(self, item):
        if item not in self._values:
            self._values.append(item)

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
