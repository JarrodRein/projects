class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid = 0
        
        # We can only start at indices where nums[i] == 0
        for start in range(n):
            if nums[start] != 0:
                continue
                
            # Try both directions: -1 (left) and +1 (right)
            for direction in [-1, 1]:
                arr = nums[:]   # copy array since we'll mutate
                curr = start
                dir = direction
                
                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += dir
                    else:
                        arr[curr] -= 1
                        dir *= -1      # reverse direction
                        curr += dir     # move in new direction
                        
                # If after walking off the array everything is zero, count it
                if all(x == 0 for x in arr):
                    valid += 1
        
        return valid
