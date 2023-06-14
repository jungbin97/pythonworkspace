# ----------------------------------------------------------------------------
# (2,2,0)는 왜 False로 => [1, 2, 1], [2, 2, 1] 에서 [2,2,1] 조건을 만족하지 않기 때문에
# ----------------------------------------------------------------------------
def check(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥 체크
            # 바닥 위 or 보의 한쪽 끝 위 or 또 다른 기둥 위라면
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            # 설치 할 수 없다면
            else:
                return False
        else:   # 설치한 구조물 보 라면
            # 해당 구조물을 설치할 수 있는지 확인(보의 한쪽 끝부분이 기둥 위거나, 양쪽 끝부분이 다른보와 동시에 연결되어있거나)
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            # 설치할 수 없다면
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    

    for x, y, a, b in build_frame:
        if b == 1:  # 구조물 설치
            answer.append([x, y, a])
            # 현재 구조물을 추가 할 수 있는 체크
            if not check(answer):
                answer.remove([x, y, a])

        elif b == 0:    # 구조물 삭제
            # 결과 구조물에서 현재 구조물 제거
            answer.remove([x, y, a])
            if not (check(answer)):
                answer.append([x, y, a])
    
    answer.sort()
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))