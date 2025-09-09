class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)   # dp[i] = number of new people who learn the secret on day i
        dp[1] = 1            # Day 1: only 1 person knows the secret
        share = 0            # running sum of people able to share
        
        for day in range(2, n + 1):
            # Add people who can start sharing today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # Remove people who forgot today
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            
            dp[day] = share  # New people who learn today = current sharers

        # Answer = people who still remember at day n
        return sum(dp[n - forget + 1 : n + 1]) % MOD
