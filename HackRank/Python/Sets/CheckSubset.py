# read A
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