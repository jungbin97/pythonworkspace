#k로 최대한 많이 나누기 
n, k = map(int, input().split())
result = 0

while n >= k:
    #n이 k로 마누어 떨어지지 않을시 1빼기
    while n % k != 0:
        n -= 1
        result += 1
    #k로 나누기
    n //= k
    result += 1


#마지막 남은 수에 대해서 1빼기
while n > 1:
    n -= 1
    result += 1
    
    
print(result)