class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == '-':
            return False