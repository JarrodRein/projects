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
                    if s == target_2: # If the sum matches the target
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # Move both pointers, skipping duplicates
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target_2: # If the sum is less than the target, move the left pointer to increase the sum
                        l += 1
                    else: # If the sum is greater than the target, move the right pointer to decrease the sum
                        r -= 1
                # End of while loop, move to the next second element
            # End of for j loop, move to the next first element

        return res # Return the list of quadruplets found
