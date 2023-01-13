T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())     # K 이동가능한 정류장 수, N 종점, M 충전소 갯수
    
    stations = list(map(int, input().split()))  # 충전소 위치 정류장 번호 입력
    count = 0
    now = 0     # 충전 횟수와 현재 위치 초기화

    # 종점에 도착할 때 까지 반복
    while now + K < N:
        # K 범위 안에 현 위치를 조정하면서 이동
        for step in range(K, 0, -1):
            if (now + step) in stations:
                # 현재 위치 변경
                now += step
                # 충전 횟수 증가
                count += 1
                break
        else:   # 충전기 설치가 잘못 되어 종점에 도달 할 수 없느 경우
            count = 0
            break

    # 결과 출력
    print("#%d %d" %(test_case, count))