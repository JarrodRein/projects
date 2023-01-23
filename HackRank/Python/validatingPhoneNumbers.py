import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    i=1
    while i <= n:
        m= str(input())
       # j = int(m)
        match = re.search(r"^[7-9][0-9]{9}$", m)
        if match:
            print("YES")
        else:
            print("NO")
       # print(m)
       # print(i, end='')
        i +=1
