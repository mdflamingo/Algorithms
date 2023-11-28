mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 8


def binary_search(mass, item):
    low = 0
    high = len(mass) - 1

    while low <= high:
        index_ser = (low + high) / 2
        value_ser = mass[index_ser]

        if value_ser == item:
            return index_ser
        if value_ser > item:
            high = index_ser - 1
        else:
            low = index_ser + 1
        return None

