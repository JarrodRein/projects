from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cubes = deque(map(int, sys.stdin.readline().split()))
    
    prev = float('inf')       # last placed cube (top of stack), start as infinity
    possible = True

    while cubes and possible:
        left, right = cubes[0], cubes[-1]
        pick = left if left >= right else right  # pick the larger end

        if pick <= prev:
            if pick == left:
                cubes.popleft()
            else:
                cubes.pop()
            prev = pick
        else:
            possible = False

    print("Yes" if possible else "No")