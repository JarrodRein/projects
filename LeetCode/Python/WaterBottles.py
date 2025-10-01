class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        empty = numBottles
        while empty >= numExchange: # While we have enough empty bottles to exchange
            n += empty // numExchange # Drink the new bottles obtained from exchange
            empty = empty // numExchange + empty % numExchange  # Update empty bottles count
        return n
# This code calculates the total number of water bottles one can drink given an initial number of bottles and an exchange rate for empty bottles.