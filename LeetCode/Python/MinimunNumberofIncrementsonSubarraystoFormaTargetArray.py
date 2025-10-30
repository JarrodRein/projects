class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        initial = len(target)
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                initial += target[i] - target[i - 1]
        return initial
    
    