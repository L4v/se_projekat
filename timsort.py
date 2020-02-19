# timsort.py
from sets import Set
''' NOTE(Jovan): Timsort algoritam
    Osobine:
        -O(nLogn) vreme soritranja
        -Stabilan algoritam
    Nacin rada:
        Niz koji se sortira deli se na blokove (RUN)
        RUN-ovi se sortiraju pomocu Insertion sorta
        Posle sortiranja RUN-ova, spajaju se pomocu 
        Merge sort-a

        Najbolje je da velicina RUN-a bude stepen 2
        kako bi Merge lepse radio
'''
# NOTE(Jovan): Velicina pojedinacnog bloka / RUN-a
RUN = 32


def _insertion_sort(arr, left, right):
    for i in range(left+1, right+1):
        temp = arr[i]
        j = i - 1
        while arr[j] < temp and j >= left:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


# NOTE(Jovan): Funkcija spajanja
def _merge(arr, l, m, r):
    # NOTE(Jovan): Delimo niz u dva dela, levi i desni
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    # NOTE(Jovan): Spajanje u veci podniz
    while i < len1 and j < len2:
        if left[i] >= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # NOTE(Jovan): Ostatak u levi / desni
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# NOTE(Jovan): Timsort
def timsort(arr):
    n = len(arr)
    for i in range(0, n, RUN):
        _insertion_sort(arr, i, min((i + 31), (n-1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = min((left + size - 1), (n-1))
            right = min((left + 2*size - 1), (n-1))
            _merge(arr, left, mid, right)
        size *= 2

