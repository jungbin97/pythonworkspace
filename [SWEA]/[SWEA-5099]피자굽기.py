# ----------------- 원형 큐 문제 ------------------------
# from collections import deque

# for test_case in range(1, int(input())+1):
#     N, M = map(int, input().split())    # N:화덕 크기 M: 피자개수

#     pizza = list(enumerate(list(map(int, input().split())), 1))   # enumerate(list[] , 1) 인덱스 1번 부터 시작
#     oven = deque()  # 오븐

#     for i in range(N):  # 오븐 크기만큼 오븐에 삽입 
#        oven.append(pizza[i]) 

#     cnt = 0
#     while len(oven)> 1:
#         i, j = oven.popleft()
#         if j != 0:
#             j = j // 2
#             oven.append((i,j))
#         elif j == 0:
#             # 피자 가져와야되는디 
#             if cnt < M-N:
#                 oven.append(pizza[N+cnt])
#                 cnt += 1
                
#     print("#{} {}".format(test_case, oven[0][0]))
# --------------------------------------------------------------
#   위에 코드 알고리즘 test_case 3번째 결과값 일치X
#   오븐 큐에서 피자를 0인지 체크하지말고 먼저 0으로 나누기
# --------------------------------------------------------------
from collections import deque

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())    # N:화덕 크기 M: 피자개수

    pizza = list(enumerate(list(map(int, input().split())), 1))   # enumerate(list[] , 1) 인덱스 1번 부터 시작
    oven = deque()  # 오븐

    for i in range(N):  # 오븐 크기만큼 오븐에 삽입 
       oven.append(pizza[i]) 

    cnt = 0
    while len(oven)> 1:
        i, j = oven.popleft()
        if j//2 != 0:
            j = j // 2      
            oven.append((i,j))
        else:
            # 피자 가져와야되는디 
            if cnt < M-N:   # 남은 피자 개수
                oven.append(pizza[N+cnt])
                cnt += 1
                
    print("#{} {}".format(test_case, oven[0][0]))
# --------------------------------------------------------------
#  enumerate함수 문법 정리
#  pizza를 deque에 넣어 남은 피자 개수를 카운트 안해주 수 있음
# 1. 2로나눈게 0이아니면 2나누고 큐뒤로 다시 삽입
# 2. 0이면 pop하고 남은 피자하나를 가져와 큐에 삽입 
# 3. 1, 2과정을 큐가 하나 남을 때까지 반복