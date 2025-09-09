from collections import namedtuple
n, cols = int(input()), input().split()
Student = namedtuple('Student', cols)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n))/n:.2f}")
