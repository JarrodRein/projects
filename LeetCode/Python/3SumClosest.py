class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        while True:
            nums.sort() 
            closest_sum = float('inf')
            n = len(nums)  
            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[left] + nums[right]
                    if abs(current_sum - target) < abs(closest_sum - target):
                        closest_sum = current_sum
                        result = closest_sum
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        current_sum = result
                        break           
            return result