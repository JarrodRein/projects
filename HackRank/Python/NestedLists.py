if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set([s[1] for s in students]))
    second_lowest = scores[1]

    result = sorted([name for name, score in students if score == second_lowest])
    for name in result:
        print(name)