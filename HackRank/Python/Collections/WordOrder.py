# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
counts = OrderedDict()

for _ in range(n):
    w = input().strip()
    counts[w] = counts.get(w, 0) + 1

# print number of distinct words
print(len(counts))
# print counts in order of first appearance
print(" ".join(str(c) for c in counts.values()))
