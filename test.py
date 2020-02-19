from sets import Set

if __name__ == '__main__':
    a = Set([1, 2, 3, 4])
    for i, item in enumerate(a):
        if item == 4:
            a[i] += 1

    print(a)
