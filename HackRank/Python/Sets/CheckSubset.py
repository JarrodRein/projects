# Enter your code here. Read input from STDIN. Print output to STDOUT


m = list(map(int, input().split()))
m = set(m)
n = int(input())
result = 'True' 
for i in range(n):
    a = set(map(int, input().split()))
    result = m.issubset(a)
print(result)
#Create a set to store unique elements
#print(m)