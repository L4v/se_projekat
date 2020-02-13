class Set:
    def __init__(self, values=None):
        self._values = [] if values is None else values

    def add(self, item):
        if item not in self._values:
            self._values.append(item)

    def __getitem__(self, index):
        return self._values[index]

    # NOTE(Jovan): AND '*'
    def __mul__(self, other):
        ret = Set()
        for i in self._values:
            if i in other and i not in ret:
                ret.add(i)
        return ret

    # NOTE(Jovan): OR '+'
    def __add__(self, other):
        ret = Set()
        for i in self._values:
            if i not in ret:
                ret.add(i)

        for i in other:
            if i not in ret:
                ret.add(i)
        return ret

    # NOTE(Jovan): NOT '-'
    def __sub__(self, other):
        ret = Set()
        for i in self._values:
            if i not in other and i not in ret:
                ret.add(i)
        return ret

    def __str__(self):
        return str('(' + ', '.join(map(str, self._values)) + ')')
