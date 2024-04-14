n = int(input())

data = set()

for _ in range(n):
    level = tuple(input().split())
    data.add(level)

print(data)

start = min([el[0] for el in data])
finish = max([el[1] for el in data])
print(start)
print(finish)