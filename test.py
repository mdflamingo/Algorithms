q = int(input())
nums = list(map(int, input().split()))

start = 0

finish = 6

max_count = 0

mass_current = nums[start:finish + 1]

while True:
    if 2 not in mass_current and 3 not in mass_current:
        all_fives = mass_current.count(5)
        if max_count < all_fives:
            max_count = all_fives
    if finish < q - 1:
        start += 1
        finish += 1

        mass_current = nums[start:finish + 1]
    else:
        break
if max_count > 0:
    print(max_count)
else:
    print(-1)

