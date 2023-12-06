from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = [str(el) for el in digits]
        tmp_digit = ''.join(tmp)
        return tmp_digit


a = Solution()
print(a.plusOne([1, 2, 3]))
