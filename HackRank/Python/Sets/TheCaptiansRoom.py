# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
m = list(map(int, input().split()))
#Create a set to store unique elements
#print(m)

captian = (n * sum(set(m)) - sum(m)) // (n - 1)
print(captian)
#captian = (n * sum(set(m)) - sum(m)) / (n -