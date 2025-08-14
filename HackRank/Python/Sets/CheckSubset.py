# Enter your code here. Read input from STDIN. Print output to STDOUT


m = set(input().split())     # A
n = int(input())
result = 'True' 
for i in range(n):
    a = set( input().split())
    if not (m < a):
        result = 'False'
        break
print(result)
#Create a set to store unique elements
#print(m)