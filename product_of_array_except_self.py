from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans_right = [1]
        ans_left = [1]

        for el in range(1, len(nums)):
            ans_right.append(ans_right[-1] * nums[el - 1])

        for el in range(len(nums)-1, -1, -1):
            t = ans_left[-1] * nums[el]
            ans_left.append(t)

        result = [x * y for x, y in zip(ans_right, list(reversed(ans_left[:len(nums)])))]

        return result


a = Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))

