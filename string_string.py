class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


a = Solution()
print(a.strStr('leetcode', 'leeto'))
        