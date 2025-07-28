def swap_case(s):
    return s.swapcase() # This method returns a new string with all uppercase letters converted to lowercase and vice versa.

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)