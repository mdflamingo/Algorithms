from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while 0 in nums1:
            nums1.remove(0)
        while 0 in nums2:
            nums2.remove(0)

        result = []
        if m == n:
            for index, el in enumerate(nums1):
                if el < nums2[index]:
                    result.append(el)
                    result.append(nums2[index])
                else:
                    result.append(nums2[index])
                    result.append(el)

        return sorted(result)


a = Solution()
print(a.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
