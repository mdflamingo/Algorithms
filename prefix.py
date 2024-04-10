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
    el_in_sort = [name for index, name in enumerate(sort_worker) if name.startswith(el[1])]
    if el[0] < len(el_in_sort):
        el_in_worker = [index + 1 for index, name in enumerate(worker) if name == el_in_sort[el[0] - 1]]
        print(*el_in_worker)
    else:
        print(-1)
