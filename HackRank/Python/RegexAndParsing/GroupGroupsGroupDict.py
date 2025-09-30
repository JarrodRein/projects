# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

s = input().strip()

m = re.search(r'([a-zA-Z0-9])\1+', s) # Search for the first alphanumeric character that appears in a group of two or more consecutive occurrences

if m:
    print(m.group(1))
else:
    print(-1)
# This code finds the first alphanumeric character that appears in a group of two or more consecutive occurrences in the input string. If such a character is found, it prints the character; otherwise, it prints -1.