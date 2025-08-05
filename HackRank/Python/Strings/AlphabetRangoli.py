import string

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    print(alphabet)
    
    #top half
    for i in range (0, size, 2):
        print((alphabet[i + size]*i).center(size,"-"))
    
    print(alphabet[0].center(size, "-"))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)