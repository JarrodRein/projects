class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:        # stop before last element
            if bits[i] == 1:
                i += 2          # skip 2-bit character
            else:
                i += 1          # skip 1-bit character

        return i == n - 1  