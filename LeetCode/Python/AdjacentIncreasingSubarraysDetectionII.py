class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Step 1: left-to-right increasing run lengths
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1
            else:
                inc[i] = 1

        # Step 2: right-to-left increasing run lengths
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1
            else:
                dec[i] = 1

        # Step 3: check boundaries
        max_k = 0
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:  # boundary between increasing runs
                left_len = inc[i - 1]
                right_len = dec[i]
                max_k = max(max_k, min(left_len, right_len))

        return max_k
