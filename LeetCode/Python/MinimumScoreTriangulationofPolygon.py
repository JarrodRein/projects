class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        minval = 0 # Initialize minval to 0
        n = len(values)
        dp = [[0] * n for _ in range(n)] # Create a 2D DP array initialized to 0
        for length in range(2, n): # Iterate over lengths from 2 to n-1
            for i in range(n - length): # Iterate over starting index i
                j = i + length # Calculate ending index j
                dp[i][j] = float('inf') # Initialize dp[i][j] to infinity
                for k in range(i + 1, j): # Iterate over possible k values between i and j
                    cost = values[i] * values[j] * values[k] + dp[i][k] + dp[k][j] # Calculate cost
                    dp[i][j] = min(dp[i][j], cost) # Update dp[i][j] with the minimum cost
        return dp[0][n - 1] # Return the minimum score for the entire polygon
