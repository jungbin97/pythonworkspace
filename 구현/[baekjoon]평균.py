import sys

n = int(sys.stdin.readline().rstrip())
grades = list(map(int, sys.stdin.readline().split()))

M = max(grades)

for i in range(len(grades)):
    grades[i] = round(grades[i]/M*100, 2)

print(sum(grades)/n)