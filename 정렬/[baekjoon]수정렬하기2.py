# ----------------------------------------------------------------------------
# [baekjoon_2751] 수 정렬하기2 (정렬, python)
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

# n = int(input().rstrip())


# arr = [int(input().rstrip()) for _ in range(n)]

# arr = sorted(arr, reverse=False)

# for i in range(len(arr)):
#     print(arr[i])
    
# ----------------------------------------------------------------------------
# 퀵정렬 시간 초과 발생

# 퀵 정렬은 최악의 경우 O(N^2)입니다.
# 이름에 quick이 있다고 속으면 안 됩니다.

# 평균 시간복잡도는 O(NlogN)이지만, 평범하게 구현한 퀵 정렬은 매우 단순한 방법으로 최악의 케이스의 시간복잡도인 O(N^2)을 만들 수 있습니다.

# 단순히 이미 정렬이나 역정렬된 상태로만 입력이 주어져도 퀵 정렬이 감당할 수 없습니다.

# 이를 회피하는 방법으로 피벗으로 중앙값의 중앙값 고르기, 재귀가 깊어지면 다른 정렬을 사용하기, 랜덤으로 섞은 뒤에 수행하기 등이 있지만 정말 잘 구현하지 않으면 여전히 효율이 매우 안 좋습니다.

# 그래서 퀵 정렬은 그냥 이 문제에 사용하지 않기를 권장합니다. 이 문제 뿐만 아니라 어떤 알고리즘 문제에도 사용하지 않는 것이 좋습니다.
# 연습하기 위한 목적으로만 쓰세요.
# ----------------------------------------------------------------------------
arr = [int(input().rstrip()) for _ in range(n)]

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start           # 피벗 초기값은 첫번째 요소

    left = start + 1        # 좌측 리스트 시작점

    right =end              # 우측 리스트 시적점

    while left <= right:
        # 피벗보다 큰 값을 찾을 때까지 무한 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        # 피벗보다 작은 값을 찾을 때까지 무한 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
            
        # 탐색하는 데이터 위치가 다른 경우
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 좌측 우측 리스트 가각 퀵 정렬 수행
    quick_sort(arr, 0, right-1) 
    quick_sort(arr, right+1, end)
    return arr


result = quick_sort(arr, 0, len(arr)-1)

for i in range(n):
    print(arr[i])