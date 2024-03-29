"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the
two numbers directly above it as shown:
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        print(res)
        for index, el in enumerate(res):
            if index == 0:
                res[index].append(1)
            elif index == 1:
                res[index].append(1)
                res[index].append(1)

        return res


a = Solution()
print(a.generate(5))
