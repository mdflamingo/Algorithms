from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indx in range(len(nums)):
            for new_indx in range(indx + 1, len(nums)):
                if nums[indx] + nums[new_indx] == target:
                    return [indx, new_indx]


obj = Solution()
print(obj.twoSum([3,2,4], 6))