n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range (0, m):
    s1 = input().strip().split()
    if s1[0] == "pop":
        s.pop()
    elif s1[0] == "remove":
        s.remove(int(s1[1]))
    elif s1[0] == "discard":
        s.discard(int(s1[1]))
#print(s)
print(sum(s))
    #print(s1)