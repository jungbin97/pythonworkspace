N, K = map(int, input().split())

result = list(map(int, input().split()))
seq = list(map(int, input().split()))

for i in range(K):
    temp = [0]*N
    for j in range(N):
        temp[seq[j]-1] = result[j]
    result = temp
    
print(*result)