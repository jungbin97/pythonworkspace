import sys
input = sys.stdin.readline

N, C = map(int,input().split())

arr = [int(input().rstrip()) for _ in range(N)]

# 이분탐색을 위해 정렬
arr.sort()

# start 최소간격, end 최대간격
start = 1
end = arr[len(arr)-1] - arr[0]
result = 0

while start <= end:
    mid = (start+end)//2 # mid은 가장 인접한 두 공유기 사이의 거리
    value = arr[0]
    count = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, N): # 앞에서 부터 설치
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= C: # C개 이상의 공유기를 설치한경우 거리를 증가
        start = mid + 1
        result = mid # 결과값 저장
    else:
        end = mid - 1 


print(result)
