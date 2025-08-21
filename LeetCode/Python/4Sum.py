class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # Sort the array to facilitate two-pointer technique and duplicate handling
        n = len(nums) # Length of the input array
        res = [] # Result list to store unique quadruplets

        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # Skip duplicate second elements
                