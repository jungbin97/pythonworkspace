# ----------------------------------------------------------------------------
# [baekjoon_1043] 거짓말
# ----------------------------------------------------------------------------
import sys
input = sys.stdin.readline

# 사람의 수, 파티의 수
n, m = map(int, input().split())

# 진실을 아는사람의 수와 번호
knows = set(input().split()[1:])


# 파티의 수만큼
party_list = []

for _ in range(m):
    party_list.append(set(input().split()[1:]))

for _ in range(m):
    for party in party_list:
        # knows과 party와 교집합이면 knows에 합집합해줌.(진실을 아는자이므로)
        if party & knows:
            knows = knows.union(party)


cnt = 0
# 파티 순회
for party in party_list:
    same_flag = False
    for i in knows:
        if i in party:
            same_flag = True
            break
    if not same_flag:
        cnt += 1

print(cnt)


# 요약
# 지민이가 거짓말쟁이로 알려지지 않으면서 과장된이야기를 할 수 있는 파티 개수 최댓값을 구하여라
# 과장된 이야기를 들으면 나중에 진짜이야기 들으면 들통남

# 풀이
# 진실을 아는자가 포함되있으면 추가(합집합), 파티 전부 순회
# 해당 파티와 비교해서 진실을 아는 번호가 존재하면 X, 없으면 cnt +1