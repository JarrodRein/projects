# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = set(int, input().split())
n1 = int(input())

for _ in range(n1):
    command = input().split()
    operation = command[0]
    num_elements = int(command[1])
    elements = set(map(int, input().split()))
    
    if operation == "update":
        m.update(elements)
    elif operation == "intersection_update":
        m.intersection_update(elements)
    elif operation == "difference_update":
        m.difference_update(elements)
    elif operation == "symmetric_difference_update":
        m.symmetric_difference_update(elements)
print(sum(m))