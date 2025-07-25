if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #adding the scores for the query_name
    #and calculating the average
    avg = sum(student_marks[query_name]) / len(student_marks[ query_name])
    print(f"{avg:.2f}")