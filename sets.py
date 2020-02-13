class Set(dict):
    def __init__(self, values=None):
        pass

    def __getattr__(self, attr):
        return self[attr]

    # NOTE(Jovan): AND '*'
    def __mul__(self, other):
        ret = Set()
        for key in self:
            if key in other:
                ret[key] = self[key]
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
