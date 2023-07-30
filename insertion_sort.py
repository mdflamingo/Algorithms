def insertion_sort(array):
    for el in range(1, len(array)):
        current_el = array[el]
        index_of_sorted = el

        while index_of_sorted > 0 and current_el < array[index_of_sorted - 1]:
            array[index_of_sorted] = array[index_of_sorted - 1]
            index_of_sorted -= 1
        array[index_of_sorted] = current_el

    print(array)


insertion_sort([11, 2, 9, 7, 1, 78])
