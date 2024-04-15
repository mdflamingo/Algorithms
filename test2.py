n, m = map(int, input().strip().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

rotated_matrix = [list(row)[::-1] for row in transposed_matrix]

for row in rotated_matrix:
    print(*row)
