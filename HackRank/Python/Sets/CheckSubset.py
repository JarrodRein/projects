# read A
# This code checks if set A is a strict superset of N sets B.
# A strict superset means A contains all elements of B and has at least one additional element
A = set(input().split())
# read N
n = int(input())

ok = True
for _ in range(n):
    B = set(input().split())
    if not (A > B):            # strict superset check
        ok = False
        break                  # early exit as soon as one fails

print(ok)