# -------------------------------------------------
#  [이코테] 위에서 아래로
# -------------------------------------------------

count = int(input())
arr = [int(input()) for _ in range(count)]

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')