# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = set(map(int, input().split()))

n1 = int(input())
m1 = set(map(int, input().split()))

print(len(m.difference(m1)))