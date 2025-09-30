class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1 # Pointer for the position of the next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: # Check if the current element is diff
                nums[k] = nums[i] # Place the unique element at position k
                k += 1 # Move the pointer for the next unique element
        return k # Return the count of unique elements
# This code removes duplicates from a sorted array in-place and returns the new length of the array with unique elements.