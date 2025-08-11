class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [
            (1000, "M"), (900, "CM"),
        (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"),
        (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"),
        (1, "I" )
        ]
            #emtpy list to store roman numeral parts
        roman_numeral = []
        #loop through the value map
        #and subtract the value from num
        for value, numeral in val_map:
            #while num is greater than or equal to value
            while num >= value:
                #append the numeral to the list
                roman_numeral.append(numeral)
                #subtract the value from num
                num -= value
        #after the loop, num should be 0
        #if not, it means num was not a valid integer

        
        #join the list into a string and return it
        return ''.join(roman_numeral)