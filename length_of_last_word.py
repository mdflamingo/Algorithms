class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = s.split(' ')
        while '' in tmp:
            tmp.remove('')
        return len(tmp[-1])



a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))
