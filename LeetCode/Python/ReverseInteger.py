class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s1 = '-' + s[:0:-1]
        else:
            s1 = s[::-1]
        return int(s1)