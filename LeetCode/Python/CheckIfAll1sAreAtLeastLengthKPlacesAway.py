class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        for num in nums:
            if num == 1:
                if count < k and count != 0:
                    return False
                count = 0
            else:
                count += 1
        return True