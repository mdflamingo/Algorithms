from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = [str(el) for el in digits]
        tmp_digit = str(int(''.join(tmp)) + 1)
        return [int(el) for el in tmp_digit]


a = Solution()
print(a.plusOne([9]))
