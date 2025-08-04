# Enter your code here. Read input from STDIN. Print output to STDOUT


n, m = map(int, input().split())
#print(line)
#print(n)

for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

print("WELCOME".center(m, "-"))

# Bottom half
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))