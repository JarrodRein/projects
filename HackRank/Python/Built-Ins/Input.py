x, k = map(int, input().split())
p = input().strip()

# Safest way: only allow 'x' as a local variable, nothing from builtins.
print(eval(p, {"__builtins__": None}, {"x": x}) == k)
