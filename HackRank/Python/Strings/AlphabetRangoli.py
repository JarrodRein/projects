import string

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    print(alphabet)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)