# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# 1) Read the input string
s = input().strip()

# 2) Build the pattern:
#    - lookbehind for a consonant
#    - capture 2+ vowels
#    - lookahead for a consonant
pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])'

# 3) Find all the vowel substrings meeting the conditions (case-insensitive)
matches = re.findall(pattern, s, flags=re.I)

# 4) Print the results or -1 if none
if matches:
    print("\n".join(matches))
else:
    print(-1)