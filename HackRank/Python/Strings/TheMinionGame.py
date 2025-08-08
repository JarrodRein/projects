def minion_game(s):
    vowels = set('AEIOU')  # or 'aeiou' if input is lowercase
    kevin = stuart = 0
    n = len(s)

    for i, ch in enumerate(s):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)