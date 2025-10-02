class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            # exchange exactly one bottle at a time
            empty -= numExchange       # spend numExchange empty bottles
            empty += 1                 # get 1 new bottle (after drinking it)
            n += 1                     # increase total drunk bottles
            numExchange += 1           # increase exchange rate
        
        return n