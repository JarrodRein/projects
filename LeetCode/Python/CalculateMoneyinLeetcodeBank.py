class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7 # number of complete weeks
        days = n % 7 # remaining days after full weeks
        
        # sum of full weeks
        # week 0 = 1..7, week 1 = 2..8, etc.
        total = 0  # initialize total amount
        for w in range(full_weeks): # sum for each full week
            total += 28 + w * 7
        
        # partial week (full_weeks is the starting add for that week)
        start = full_weeks + 1
        for d in range(days):
            total += start + d
        
        return total