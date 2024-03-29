"""
Given a non-empty array of integers nums,
every element appears twice except for one. Find that single one.
You must implement a solution with a
linear runtime complexity and use only constant extra space.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for el in nums:
            if el in result:
                result[el] += 1
            else:
                result[el] = 1
        for num in result:
            if result[num] == 1:
                return num


a = Solution()
print(a.singleNumber([4, 1, 2, 1, 2]))
