# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
m = int(input())

angle_MBC = math.degrees(math.atan2(n, m))
print(int(angle_MBC))   