# ----------------------------------------------------------------------------
# [baekjoon_14226] 이모티콘
# ----------------------------------------------------------------------------
from collections import deque

S = int(input())
visited = [[0] * 1001 for _ in range(1001)]
answer = 0

def bfs():
    q = deque()
    # 화면의 이모지 개수, 클립보드 이모지 개수
    q.append((1, 0))
    global answer
    while q:
        screen_len, clip_len = q.popleft()

        # 탈출 조건
        if screen_len == S:
            answer = visited[screen_len][clip_len]
            break

        # 복사, 붙여넣기, 삭제
        tmp = [(screen_len, screen_len), (screen_len + clip_len, clip_len), (screen_len-1, clip_len)]

        for nx_screen_len, nx_clip_len in tmp:
            if 0 <= nx_screen_len < 1001 and 0 <= nx_clip_len < 1001 and not visited[nx_screen_len][nx_clip_len]:
                q.append((nx_screen_len, nx_clip_len))
                visited[nx_screen_len][nx_clip_len] = visited[screen_len][clip_len] + 1
    return answer

bfs()
print(answer)

# 요약
# 이모티콘 한개로 주어진 S개의 개수로 만드는 법을 구하여라
# 1. 화면에 있는 이모티콘 모두 클립보드에 복사
# 2. 클립보드에 있는 모든 이모티콘을 붙여넣기
# 3. 화면에 있는 이모티콘 하나 삭제
#
# 위의 연산은 모두 1초걸림. 필요한 최소시간을 구하여라



# 풀이
# 1 -> 2 -> 4 -> 8 -> 16 ...
# 범위가 2 <= S =<1000
# 복, 붙, 삭제
#
# 큐에 복, 붙, 삭제 넣고 S도달하면 시간 출력 q.append((화면 이모지 개수, 클립보드 이모지 개수))