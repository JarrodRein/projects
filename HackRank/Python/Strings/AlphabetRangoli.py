import string

def print_rangoli(size):
    # your code goes here
    alphabet = list(string.ascii_lowercase)
    #print(alphabet)
    width = 4 * size - 3  # total width of each line

    # top half
    for i in range(size - 1, 0, -1):
        # sequence[start:stop:step]
        left = alphabet[size-1:i:-1]
        center = alphabet[i:size]
        line = '-'.join(left + center)
        print(line.center(width, '-'))
    #sequence[start:stop:step]
    full = alphabet[size-1::-1] + alphabet[1:size]
    print('-'.join(full).center(width, '-'))
        
    for i in range (1, size):
        left = alphabet[size-1:i:-1]
        center = alphabet[i:size]
        line = '-'.join(left + center)
        print(line.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)