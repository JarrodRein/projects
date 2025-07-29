def swap_case(s):
    return s.swapcase() # This method returns a new string with all uppercase letters converted to lowercase and vice versa.

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#manually scripted
# This function iterates through each character in the string `s`, checks if it is lowercase or uppercase, and swaps the case accordingly.
    # The result is then printed.
def swap_case(s):
    result = ''
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result