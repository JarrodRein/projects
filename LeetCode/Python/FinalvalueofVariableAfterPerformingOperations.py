class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 # initial value
        for op in operations:
            if op[1] == '+': # either "++X" or "X++" are in the same place
                x += 1 # increment
            else: # either "--X" or "X--" are in the same place and be deduced
                x -= 1
        return x
    