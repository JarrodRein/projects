import textwrap

def wrap(string, max_width):
    for i in (len(string)+1 - max_width):
        print(string[i:i-len(string)])   
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)