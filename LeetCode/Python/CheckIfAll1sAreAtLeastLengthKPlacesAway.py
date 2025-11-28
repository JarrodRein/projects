class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0 # Count of zeros between 1s
        for num in nums:
            if num == 1:
                if count < k and count != 0: #check if there are enough zeros between 1s
                    return False #not enough zeros return False
                count = 0 #reset count after encountering a 1
            else:
                count += 1 #increment count for zeros
        return True #all 1s are at least k places away