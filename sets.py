class Set:
    def __init__(self, values=None):
        self._values = [] if values is None else values

    # NOTE(Jovan): AND '*'
    def __mul__(self, other):
        ret = []
        for i in self._values:
            if i in other and i not in ret:
                ret.append(i)
        return Set(ret)

    # NOTE(Jovan): OR '+'
    def __add__(self, other):
        ret = []
        for i in self._values:
            if i not in ret:
                ret.append(i)

        for i in other:
            if i not in ret:
                ret.append(i)
        return Set(ret)

    # NOTE(Jovan): NOT '-'
    def __sub__(self, other):
        ret = []
        for i in self._values:
            if i not in other and i not in ret:
                ret.append(i)
        return Set(ret)
