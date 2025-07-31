if __name__ == '__main__':
    s = input()
    
    # Check if any character is alphanumeric
    for c in s:
        if c.isalnum():
            print("True")
            break
    else:
        print("False")

    # Check if any character is alphabetic
    for c in s:
        if c.isalpha():
            print("True")
            break
    else:
        print("False")

    # Check if any character is a digit
    for c in s:
        if c.isdigit():
            print("True")
            break
    else:
        print("False")

    # Check if any character is lowercase
    for c in s:
        if c.islower():
            print("True")
            break
    else:
        print("False")

    # Check if any character is uppercase
    for c in s:
        if c.isupper():
            print("True")
            break
    else:
        print("False")