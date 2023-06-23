n, m = map(int, input().split())
l = []
count = []

# 체스판 입력받기
for _ in range(n):
    l.append(input())

for i in range(n-7):
    for j in range(m-7):
        index1 = 0  # 시작 지점이 검은색일떄 검은색이 아니게되면 +1
        index2 = 0  # 시작 지점이 흰색일때 흰색이 아니게 되면 +1
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b)% 2 == 0:
                    if l[a][b] != 'B':
                        index1 += 1
                    if l[a][b] != 'W':
                        index2 += 1
                else:
                    if l[a][b] != 'W':
                        index1 += 1
                    if l[a][b] != 'B':
                        index2 += 1

        count.append(index1)
        count.append(index2)

print(min(count))