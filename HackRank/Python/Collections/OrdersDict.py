# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
orders = OrderedDict()
for _ in range(n):
    item, price = input().rsplit(' ', 1)
    price = int(price)
    if item in orders:
        orders[item] += price
    else:
        orders[item] = price

for item, total_price in orders.items():
        print(item, total_price)
        