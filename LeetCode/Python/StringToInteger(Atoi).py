class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1 
        i = 0
        result = 0

        if s[0] =='-':
            sign = -1
            i += 1
        elif s[0] =='+':
            i += 1
            #loops through the string and detects digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i +=1

        result *= sign

        # Check 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Return result within the 32-bit signed integer range
        # could be if elif or just if
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result