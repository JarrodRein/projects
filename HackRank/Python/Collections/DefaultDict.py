# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n+1):
    word = input().strip()
    d[word].append(i)
for j in range(m):
    query = input().strip()
    if query in d:
        print(' '.join(map(str, d[query])))
    else:
        print(-1)