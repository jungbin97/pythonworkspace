#k로 최대한 많이 나누기(1빼기 간소화)
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)      # 2 - 0 발생

    n = target
    # 더이상 나눌 수 없을 때까지
    if n < k:
        break
    #k로 나누기
    result += 1
    n //= k

result += (n-1)

print(n)
print(result)