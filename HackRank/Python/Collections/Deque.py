# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()

n = int(input())
for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'append':
        d.append(int(cmd[1]))
    elif cmd[0] == 'appendleft':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        d.pop()
    elif cmd[0] == 'popleft':
        d.popleft()
    elif cmd[0] == 'clear':
        d.clear()
    elif cmd[0] == 'extend':
        d.extend(map(int, cmd[1:]))
    elif cmd[0] == 'extendleft':
        d.extendleft(map(int, cmd[1:]))
    elif cmd[0] == 'remove':
        d.remove(int(cmd[1]))
    elif cmd[0] == 'rotate':
        d.rotate(int(cmd[1]))
print(*d)
