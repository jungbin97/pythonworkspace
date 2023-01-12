num = int(input())

cnt = [0 for _ in range(10)]

for i in range(6):
    cnt[num % 10] += 1
    num //= 10

i = 0
tri = 0
run = 0

while i < 10:
    if cnt[i] >= 3:
        cnt[i] -= 3
        tri += 1
        continue
    if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1: # run 조사 후 데이터 삭제
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("baby gin")
else:
    print("lose")
