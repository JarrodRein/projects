class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):   # start from 2nd-to-last row up to 0
            for col in range(len(triangle[row])):     # each element in that row
                triangle[row][col] += min(
                    triangle[row + 1][col],           # left child
                    triangle[row + 1][col + 1]        # right child
                )
        return triangle[0][0]