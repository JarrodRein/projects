class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        mods = [0] * value
        for num in nums:
            mod = num % value
            if mod < 0:
                mod += value
            mods[mod] += 1

        ans = 0
        while True:
            mod = ans % value
            if mods[mod] == 0:
                return ans
            mods[mod] -= 1
            ans += 1