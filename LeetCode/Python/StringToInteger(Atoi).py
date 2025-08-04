class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0