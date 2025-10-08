from bisect import bisect_left
    
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # O(n log n)
        m = len(potions)
        res = []
        for spell in spells: # O(m log n)
            min_potion = (success + spell -1) //spell # ceiling division
            idx = bicect_left(potions, min_potion) # O(log n)
            count = m - idx # number of successful pairs
            res.append(count)  # O(1)
        return res # O(m log n + n log n) time, O(1) space
    
