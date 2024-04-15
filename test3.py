def print_directories(directories):

    for directory in directories:
        prefix_count = len(directory) - 1
        print(('  ' * prefix_count) + directory[-1])


n = int(input())
directories = []

for _ in range(n):
    directories.append(input().split('/'))

directories.sort()

print_directories(directories)

