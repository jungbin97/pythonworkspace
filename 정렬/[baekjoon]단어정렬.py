n = int(input())
str = []

for i in range(n):
    str.append(input())

str1 = list(set(str))
str1.sort()
str1.sort(key=lambda x : len(x))

for i in str1:
    print(i)