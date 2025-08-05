import string

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    #print(alphabet)
    
    #top half
    for i in range (size-1, 0, -1):
        print((alphabet[i]).center(size,"-"))
    
    print(alphabet[0].center(size, "-"))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)