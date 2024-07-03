from typing import List


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for el in nums:
            if el in dict_nums:
                dict_nums[el] += 1
            else:
                dict_nums[el] = 1

        for el in dict_nums:
            if dict_nums[el] != 1:
                return True
        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        return False


obj = Solution1()
print(obj.containsDuplicate([1, 2, 3, 1]))
