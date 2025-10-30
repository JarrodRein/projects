class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        initial = target[0] # initial increments to reach first element
        for i in range(1, len(target)):    # iterate through target
            if target[i] > target[i - 1]: # if current is greater than previous
                initial += target[i] - target[i - 1] # add difference to initial
        return initial # return total increments needed
    
