# ----------------------------------------------------------------------------
# [baekjoon_17276] 배열 돌리기(구현, python) 
# 파이썬 음수의 나머지 계산 원리르 알아야한다.
#
# # 회전 횟수 음에서 -> 양으로 변환 할 때
# count = 8-(d%360)//45 하지 않아도 되는 이유
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

# 테스트 케이스 입력
test_case = int(input().rstrip())

def rotation(arr, n):
    temp = []
    for i in range(n):
        # 주대각선 저장
        temp.append(arr[i][i])

    # 주대각선 -> 가운데 열
    for i in range(n):
    # 배열 값하나씩 체인지
        temp2 = arr[i][n//2]
        arr[i][n//2] = temp[i]
        # 가운데 열에 있던 값
        temp[i] = temp2
    
    temp.reverse()
    # 가운데 열 -> 부 대각선
    for i in range(n):
        
        temp2 = arr[n-1-i][i]
        arr[n-1-i][i] = temp[i]  # 수정 필요 => temp.reverse() 로 해결!
        temp[i] = temp2

    # 부 대각선 -> 가운데 행
    for i in range(n):
        temp2 = arr[n//2][i]
        arr[n//2][i] = temp[i]
        arr[i][i] = temp2
    

for _ in range(test_case):
    # 배열 크기 n , 각도 d
    n, d = map(int, input().rstrip().split())

    # 리스트 초기화
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    count = (d%360)//45
    # 음수 일때(-45도=> 시계방향으로 315도 회전 =>7번)

    # 0이면 루프 탈출
    while count:
        # 시계 방향으로 회전
        if count > 0:
            count -= 1
            rotation(arr, n)

    for row in arr:
        print(*row)