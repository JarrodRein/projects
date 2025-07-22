if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
       # print(name)

    scores = [s[1] for s in students]
    sorted(scores)
    second_lowest = scores[1]
    #print(score[1])

    result = [name for name, score in students if score == second_lowest]
    sorted(result)
    for name in result:
        print(name)