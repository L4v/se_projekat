def and_items(a, b):
    return list(set(a).intersection(b))


def or_items(a, b):
    return list(set(a + b))


def not_items(a, b):
    return list(set(a) - set(b))
