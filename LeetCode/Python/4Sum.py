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
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Two pointers for the other two elements
                target_2 = target - nums[i] - nums[j]
                l, r = j + 1, n - 1  # Two pointers start after the second element and at the end of the list
                # Move pointers towards each other
                while l < r: # Ensure pointers do not cross
                    s = nums[l] + nums[r] # Calculate the sum of the two elements
                   