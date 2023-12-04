from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] > target:
            return 0
        elif target not in nums:
            for index, element in enumerate(nums):
                if index == len(nums) - 1:
                    return index + 1
                elif element < target < nums[index + 1]:
                    return index + 1
                elif element > target:
                    return index
        else:
            for index, element in enumerate(nums):
                if target == element:
                    return index


a = Solution()
print(a.searchInsert([1], 0))
