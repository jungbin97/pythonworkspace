# ---------------------------------------------
#  이진탐색 소스 코드(재귀 구현)
# ---------------------------------------------

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
# n(원소개수)과 target(찾고자하는 숫자)를 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행결과 출력
result = binary_search(array, target, 0, n-1)   # n-1 은 마지막 인덱스 번호(인덱스 번호로 나누기 때문에)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)