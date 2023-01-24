#n동전 갯수, k총합 입력
n, k = map(int, input().split())
count = 0
#동전 가치 입력

a = []
for i in range(n):
    a.append(int(input()))
    
a.reverse()

#k를 큰 수 부터 나누기
for coin in a:
    count += k//coin
    k %= coin
    
print(count)