class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        results = []
        n = len(nums)
        for i in range(0, n-1):
            current = nums[i]
            for j in range(i+1, n):
                if current == nums[j] and current not in results:
                    results.append(current)
        return results