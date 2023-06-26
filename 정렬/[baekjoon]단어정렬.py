import sys

n = int(sys.stdin.readline().rstrip())
str = []

for i in range(n):
    str.append(sys.stdin.readline().rstrip())

str1 = list(set(str))
str1.sort()
str1.sort(key=lambda x : len(x))

for i in str1:
    print(i)