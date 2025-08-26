class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        if n % 2 != 0:
            return False
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        