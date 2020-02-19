from timsort import timsort, insertion_sort

if __name__ == '__main__':
    items = []
    for i in range(0, 100):
        items.append(i)
    timsort(items)
    print(items)
