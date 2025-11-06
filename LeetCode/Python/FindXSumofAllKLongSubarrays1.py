class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        window_sum = sum(nums[:k])
        if window_sum == x:
            result.append(0)
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            if window_sum == x:
                result.append(i - k + 1)
        return result