class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        empty = numBottles
        while empty >= numExchange:
            n += empty // numExchange
            empty = empty // numExchange + empty % numExchange
        return n
# This code calculates the total number of water bottles one can drink given an initial number of bottles and an exchange rate for empty bottles.