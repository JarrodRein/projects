class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        empty = numBottles
        while empty >= numExchange: # While we have enough empty bottles to exchange
            n += empty // numExchange # Drink the new bottles obtained from exchange
            empty = empty // numExchange + empty % numExchange  # Update empty bottles count
            numExchange += 1  # Increase the exchange rate by 1 after each exchange
        return n