class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # inc[i] = length of strictly increasing run ending at i
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        # dec[i] = length of strictly increasing run starting at i
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1

        # Try every split (between i-1 and i), no boundary restriction
        ans = 0
        for i in range(1, n):
            ans = max(ans, min(inc[i - 1], dec[i]))

        return ans
