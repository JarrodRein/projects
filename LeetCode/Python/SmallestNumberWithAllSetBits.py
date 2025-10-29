class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 0 
        for i in range(n):
            result |= (1 << i)
        return result
    