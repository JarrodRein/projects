class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # Try k operations, 1..60
        for k in range(1, 61):
            t = num1 - k * num2
            if t < k:                 # can't make t with k powers since each >= 1
                continue
            if t >= 0 and t.bit_count() <= k:
                return k
        return -1