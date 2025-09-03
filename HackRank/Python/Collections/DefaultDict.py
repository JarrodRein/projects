# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list) # default value is an empty list

n, m = map(int, input().split()) # n = number of words, m = number of queries

for i in range(1, n+1): # i is the line number, starting from 1, n is inclusive
    word = input().strip() # read the word
    d[word].append(i) # append the line number to the list of the word
for j in range(m): # for each query
    query = input().strip() # read the query
    if query in d: # if the query is in the dictionary
        print(' '.join(map(str, d[query]))) # print the line numbers as space-separated values
    else: # if the query is not in the dictionary
        print(-1)