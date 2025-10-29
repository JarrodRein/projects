class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1 # number of bits
        while (1 << x ) - 1 < n: # all bits set
            x+=1 # increment number of bits
        return (1 << x ) - 1 # return number with all bits set
    