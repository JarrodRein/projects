# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
# read English subscribers
n = int(input())
E = set(map(int, input().split()))

# read French subscribers
b = int(input())
F = set(map(int, input().split()))

# number of students with at least one subscription = |E F|
print(len(E | F)) 

# EOF