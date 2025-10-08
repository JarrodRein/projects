import re

S = input()
k = input()

pattern = f'(?=({k}))'
matches = list(re.finditer(pattern, S))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))
