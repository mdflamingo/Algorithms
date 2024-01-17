"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = [el for el in s.lower() if el.isalnum()]
        return new_str == new_str[::-1]


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
