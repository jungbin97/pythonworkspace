# ----------------------------------------------------------------------------
# [programmers]단속 카메라 (그리디, python)
# - 진출지점 기준으로 정렬 오름차순(진출지점기준으로 오름차순으로 정렬해야 
# 진출지점에 카메라가 있다고 가정 했을 때 그 이후에 경로의 진입지점이 진출지점보다 앞에 있어야 하기 때문에)
# ----------------------------------------------------------------------------
# def solution(routes):
#     answer = 0
#     routes.sort(key = lambda x: x[1])
#     # 기준 제한사항 참조
#     key = -30001
#     # 필요한 카메라 수
#     cnt = 0

#     for route in routes:
#         # 기준(카메라)보다 진입지점이 뒤에 있으면
#         if route[0] > key:
#             # 단속이 안되기떄문에 카메라 설치
#             cnt += 1
#             # 새로운 기준은 해당 경로의 진출지점(맨끝)
#             key = route[1]

#     return cnt

# print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

# ----------------------------------------------------------------------------
# 다른 풀이
# 위 풀이와 동일하나 가독성 좋음
# ----------------------------------------------------------------------------
def solution(routes):
    # routes를 진출지점 기준으로 오름차순 정렬
    routes.sort(key = lambda x : x[1])
    answer = 1
    # camera = 현재 카메라 위치
    camera = routes[0][1]

    # 두 번째 차량 부터 마지막번째 차량까지 반복문을 돌며 현재 카메라 위치 보다
    # 뒤에 있으면 camera에 현재 차량의 진출지점을 위치 해주고 answer += 1한다.
    for i in range(1, len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            answer += 1

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))