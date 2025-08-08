def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(string), 1):
        if string[i] in vowels:
            kevin_score = len(string) - i
            if 'kevin' in locals():
                kevin += kevin_score
            else:
                kevin = kevin_score
        else:
            stuart_score = len(string) - i
            if 'stuart' in locals():
                stuart += stuart_score
            else:
                stuart = stuart_score
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)