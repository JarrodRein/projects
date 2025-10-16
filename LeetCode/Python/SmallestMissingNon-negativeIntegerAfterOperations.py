class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums) # of elements
        mods = [0] * value # mods[i] = count of elements with num % value == i
        for num in nums: # O(n)
            mod = num % value # Python's % can be negative
            if mod < 0: # make it positive
             mod += value # now 0 <= mod < value
            mods[mod] += 1 # count it

        ans = 0 # candidate answer
        while True:     # O(n) iterations, at most
            mod = ans % value # we need at least one element with this mod
            if mods[mod] == 0: # no such element
                return ans # this is the answer
            mods[mod] -= 1 # use one such element
            ans += 1 # try next answer