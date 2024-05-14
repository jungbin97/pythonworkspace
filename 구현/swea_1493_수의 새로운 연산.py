# ----------------------------------------------------------------------------
# D3[swea_1493] 수의 새로운 연산
# ----------------------------------------------------------------------------
# for tc in range(1, int(input())+1):
#     p, q = map(int, input().split())
#     graph = [[0] * 300 for _ in range(300)]
#
#     cnt = 0
#     for k in range(300):
#         for i in range(0, k+1):
#             cnt += 1
#             graph[k-i][i] = cnt
#
#             if p == cnt:
#                 x1, y1 = k-i+1, i+1
#             if q == cnt:
#                 x2, y2 = k-i+1, i+1
#
#     x3, y3 = x1+x2, y1+y2
#     result = graph[x3-1][y3-1]
#
#     print(f"#{tc} {result}")

i, j = 1, 1
xy_to_num = {}
num_to_xy = {}
for n in range(1, 50000):
    num_to_xy[n] = (i, j)
    xy_to_num[(i, j)] = n
    i, j = i-1, j+1
    if i < 1:
        i, j = j, 1

for tc in range(1, int(input())+1):
    p, q = map(int, input().split())

    pi, pj = num_to_xy[p]
    qi, qj = num_to_xy[q]

    result = xy_to_num[(pi+qi, pj+qj)]
    print(f"#{tc} {result}")


# [0][0]
# [1][0] [0][1]
# [2][0] [1][1] [0][2]
#
# 풀이
# 리스트는 어떻게 구성? 최대값을 모른다. 삼각형으로 구성되므로 삼각형 10000이면 150 X 150개 구하면 얼추 맞음
# 그러나 p+q의 좌표가 (150,0) + (150,0) => (300, 0)임 300 * 300  대충 50000개 구하면됨.

# 리스트를 만듬 p, q의 좌표를 구하고, 해당 좌표들을 연산 (x1, y1) + (x2, y2) = (x3, y3)
# 해당 좌표의 순서를 출력하면된다.

