from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        curr = 0
        if nums[curr] == 0:
            return self.countValidSelections(nums[:curr] + nums[curr+1:])
        elif nums[curr] > 0:
            count = 0
            for i in range(curr + 1, len(nums)):
                if nums[i] < 0:
                    nums[i] += 1
                    count += self.countValidSelections(nums[:curr] + nums[curr+1:])
                    nums[i] -= 1
            return count
        else:
            count = 0
            for i in range(curr + 1, len(nums)):
                if nums[i] > 0:
                    nums[i] -= 1
                    count += self.countValidSelections(nums[:curr] + nums[curr+1:])
                    nums[i] += 1
            return count
       