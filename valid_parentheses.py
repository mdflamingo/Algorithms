class Solution1:
    def isValid(self, s: str) -> bool:

        while len(s) > 0:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if len(s) != 0:
                return False
            return True


class Solution2:
    def isValid(self, s: str) -> bool:
        true_seq = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        tmp = []
        for letter in s:
            if letter not in true_seq:
                if not tmp or true_seq[tmp.pop()] != letter:
                    return False
            else:
                tmp.append(letter)
        return len(tmp) == 0


obj = Solution1()
print(obj.isValid('()[]{}'))

