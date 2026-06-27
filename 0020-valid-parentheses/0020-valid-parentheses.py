class Solution:
    def isValid(self, s: str) -> bool:
        values = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stk = []

        for ch in s:
            if ch in values:
                stk.append(ch)
            else:
                if not stk or values[stk[-1]] != ch:
                    return False
                stk.pop()

        return len(stk) == 0