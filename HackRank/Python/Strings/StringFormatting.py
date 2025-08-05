def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        # Decimal
        deci = str(i)
        # Octal
        octa = oct(i).replace("0o", "")
        # Hexadecimal
        hexa = hex(i).replace("0x", "").upper()
        # Binary
        bina = bin(i).replace("0b", "")
        # Width for formatting
        width = len(bin(number).replace("0b", ""))
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)