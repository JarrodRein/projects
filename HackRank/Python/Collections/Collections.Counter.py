from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
integer_list = map(int, input().split())
items = Counter(integer_list)
m = int(input())
total = 0
for _ in range(m):
    a, b = map(int, input().split())

    