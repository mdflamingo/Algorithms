import re

n = int(input())
q = int(input())

worker = []
requests = []

for _ in range(n):
    worker.append(input())

for _ in range(q):
    res = input().split()
    requests.append((int(res[0]), res[1]))

sort_worker = sorted(worker)
for el in requests:
    el_in_sort = [name for name in sort_worker if name.startswith(el[1])]
    print(el_in_sort)
    res = [el[index] for index, el in enumerate(el_in_sort) if len(el_in_sort) > 1]
    print(res)
    # el_in_worker = [index for index, name in enumerate(worker) if name.startswith(el_in_sort[el[0]])]
    # print(el_in_worker)
