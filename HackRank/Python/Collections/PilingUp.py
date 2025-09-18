# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for _ in range(n):
    m = int(input())
    l = list(map(int, input().split()))

    for i in range(m):
        if l[0] >= l[-1]:
            l.pop(0)
        else:
            l.pop()
        if not l:
            print("Yes")
            break

        if l[0] < l[-1]:
            print("No")
            break  

        else:
            print("Yes")    
    