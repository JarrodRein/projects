if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
       # print(name)

    unique_scores = sorted(set(score for name, score in students))

    # Step 2: Get the second lowest score
    second_lowest = unique_scores[1]

    # Step 3: Get names of students with that score, sorted alphabetically
    result = sorted([name for name, score in students if score == second_lowest])

    # Step 4: Print each name on a new line
    for name in result:
        print(name)