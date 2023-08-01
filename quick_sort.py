def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [el for el in array[1:] if el <= pivot]
        right = [el for el in array[1:] if el >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([4, 8, 9, 20, 1, 5, 3, 10]))

n = int(input())
for player in range(n):
    data = input().split()
