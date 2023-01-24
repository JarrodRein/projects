if __name__ == '__main__':
    N = int(input())

lis = []
for i in range(0, N):
    m = input().split()
   # print(m[0] + m[1] +m[2])
    if m[0]=='insert':
        lis.insert(int(m[1]),int(m[2]))
    if m[0]=='remove':
        lis.remove(int(m[1]))
    if m[0]=='append':
        lis.append(int(m[1]))
    if m[0]=='sort':
        lis.sort()
    if m[0]=='pop':
        lis.pop()
    if m[0]=='reverse':
        lis.reverse()     
    if m[0]=='print':
        print(lis)
