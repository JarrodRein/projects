class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 

        return result
# --- IGNORE ---