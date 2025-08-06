class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) >= len(p):
            return False