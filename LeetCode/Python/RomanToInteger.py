class Solution:
    def romanToInt(self, s: str) -> int:
        val_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        #initialize total and previous value
        total = 0
        prev_value = 0
        #loop through the string in reverse order
        for char in reversed(s):
            #get the value from the map
            value = val_map[char]
            #if the value is less than the previous value, subtract it
            #otherwise, add it
            if value < prev_value:
                total -= value
            else:
                total += value
            #update the previous value
            prev_value = value
        
        return total