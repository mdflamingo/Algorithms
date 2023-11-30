from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set()
        unique_index = 0

        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
                nums[unique_index] = num
                unique_index += 1

        return unique_index


a = Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
