from typing import List
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for index, element in enumerate(nums[1:]):
            t = nums[:index]
            print(t)
            r = math.prod(nums[index:])
            left.append(r)

        for index, element in enumerate(nums[::1]):
            right.append(nums[index - 1])

        # print(left)
        # print(right)
        return left


a = Solution()
print(a.productExceptSelf([1, 2, 3, 4]))

