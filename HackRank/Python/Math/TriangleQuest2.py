# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

n = int(input())

for i in range(1, n+1):
    print(((10**i - 1)//9)**2)