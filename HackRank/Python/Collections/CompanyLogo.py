from collections import Counter

s = input().strip()

# count each character
cnt = Counter(s)

# sort by (-frequency, character) and take top 3
for ch, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(ch, c)