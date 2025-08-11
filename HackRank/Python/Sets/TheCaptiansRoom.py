# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
m = list(map(int, input().split()))
#Create a set to store unique elements
#print(m)

captian = (n * sum(set(m)) - sum(m)) // (n - 1)
print(captian)
#captian = (n * sum(set(m)) - sum(m)) / (n -

# bigger O(n)) solution
# for room, c in counts.items():
#     if c == 1:    
#         print(room)
from collections import Counter

K = int(input())
rooms = list(map(int, input().split()))

counts = Counter(rooms)
for room, c in counts.items():
    if c == 1:
        print(room)
        break