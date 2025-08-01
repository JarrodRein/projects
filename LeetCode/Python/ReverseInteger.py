class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s1 = '-' + s[:0:-1]
        else:
            s1 = s[::-1]
        result = int(s1)

        # Check 32-bit signed integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result