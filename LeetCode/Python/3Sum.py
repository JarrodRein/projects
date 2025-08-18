class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # First element cannot repeat
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Two pointers for the other two elements
            target = -nums[i]
            l, r = i + 1, n - 1 # Two pointers start after the first element and at the end of the list
            # Move pointers towards each other

            while l < r: # Ensure pointers do not cross
                # Calculate the sum of the three elements
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move both pointers, skipping duplicates
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < target: # If the sum is less than the target, move the left pointer to increase the sum
                    l += 1
                else:
                    r -= 1
            # End of while loop, move to the next first element
        # Return the list of triplets found
        return res