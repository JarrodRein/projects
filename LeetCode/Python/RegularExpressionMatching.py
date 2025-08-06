class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #if string is bigger than pattern. Then return false. Has to be 1 - 1
        if not p:
            return not s
        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

        if len(p) >=2 and p[1] =='*':
            # Try zero occurrence of p[0] (i.e., skip 2 in pattern)
            # Or, if match, move string forward
            return (self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p)))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        