class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        space_count = s.count(' ')

        if not s:
            return 0
        elif space_count > 0:
            return 1

        s = s.replace(' ', '')
        max_substr = []
        substr = ''

        for el in s:
            if el not in substr:
                substr += el
            else:
                max_substr.append(len(substr))
                substr = ''
                substr += el
        return max(max_substr)


obj = Solution()
print(obj.lengthOfLongestSubstring(""))
