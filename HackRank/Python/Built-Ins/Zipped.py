# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())


mark = []
for i in range (X):
    mark.append(list(map(float, input().split())))

for i in zip(*mark):
    print("{:.1f}".format(sum(i)/len(i)))
