from collections import Counter

s = input().strip()

# count each character
cnt = Counter(s)

# sort by (-frequency, character) and take top 3
for ch, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(ch, c)

    cnt.items() #gives a list of pairs like [('b', 3), ('a', 2), ('c', 1), ('d', 1), ('e', 1)].

# We sort with a custom key:
# -x[1] means sort by frequency descending (higher counts first). The minus sign reverses the normal ascending order.
# x[0] means if two characters have the same frequency, sort by the character itself in alphabetical order.