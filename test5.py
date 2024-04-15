def max_mushrooms(grid, n):
    dp = [[0] * 3 for _ in range(n)]
    for i in range(n):
        for j in range(3):
            if grid[i][j] == 'W':
                continue
            if i == 0:
                dp[i][j] = int(grid[i][j] == 'C')
            else:
                left = dp[i-1][max(0, j-1)]
                mid = dp[i-1][j]
                right = dp[i-1][min(2, j+1)]
                dp[i][j] = max(left, mid, right) + int(grid[i][j] == 'C')
    return max(dp[-1])


n = int(input())

road = []

for _ in range(n):
    string = list(input())
    road.append(string)

print(max_mushrooms(road, n))
