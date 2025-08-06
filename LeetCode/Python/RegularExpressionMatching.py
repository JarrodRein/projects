class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #if string is bigger than pattern. Then return false. Has to be 1 - 1
        if len(s) > len(p):
            return False
        else:
            return True
        