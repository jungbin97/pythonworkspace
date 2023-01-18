# bit shift로 부분집합 만들기
arr = [3,6,7,1,5,4]
n=len(arr)

for i in range(1<<n):    # [000000] ~ [111111]
    for j in range(n):
        if i&(1<<j):    # [1] [10] ~ [100000] 해당자리 비트 넣을지 확인
            print(arr[j], end=",")
    print()