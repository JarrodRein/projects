class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = n // 7
        day = n % 7
        for i in range(n):
            total += week + (i % 7) + 1
        return total