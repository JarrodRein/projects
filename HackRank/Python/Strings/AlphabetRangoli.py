import string

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    #print(alphabet)
    width = 4 * size - 3  # total width of each line

    # top half
    for i in range(size - 1, 0, -1):
        left = alphabet[size-1:i:-1]
        center = alphabet[i:size]
        line = '-'.join(left + center)
        print(line.center(width, '-'))
    
    print(alphabet[0].center((size -1) *(size-1),"-"))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)