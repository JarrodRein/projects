# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s = set(map(int, input().split()))
m = int(input())
s2 = set(map(int, input().split()))

# Calculate the intersection of two sets
print(len(s.intersection(s2)))