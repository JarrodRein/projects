# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input()) # Number of test cases
pattern = r'^[+-]?(\d*\.\d+|\d+\.\d+)$' # Pattern to match only floating point numbers
for _ in range(n):
    s = input().strip()
    if s == "0":
        print(False)
        continue
    if re.match(pattern, s):
        print(True)
    else:
        print(False)