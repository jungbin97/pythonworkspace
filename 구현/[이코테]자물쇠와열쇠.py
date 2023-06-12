# ----------------------------------------------------------------------------
#  rotation() 함수 부분이 효율성 문제 발생
# ----------------------------------------------------------------------------
# def rotation(array):
#     n = len(array)  # 배열의 길이

#     result = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):  # 결과 리스트
#             result[j][n-i-1] = array[i][j]
#     return result

# # 자물쇠 중간이 부분이 모두 1인지 체크
# def check(new_lock):
#     LockLength = len(new_lock)//3

#     for i in range(LockLength, LockLength*2):
#         for j in range(LockLength, LockLength*2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n  = len(lock)
#     m = len(key)

#     # 자물쇠 크기를 기존의 3배로 불리기
#     new_lock = [[0]*(n*3) for _ in range(n*3)]
#     # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
#     for i in range(n):
#         for j in range(n):
#             new_lock[n+i][n+j] = lock[i][j]

#     # 열쇠 (1,1)부터 (n*2, n*2)까지 이동시키며 확인
#     for i in range(1, n*2):
#         for j in range(1, n*2):
#             # 열쇠를 0, 90, 180, 270도록 회전
#             for _ in range(4):
#                 r_key = rotation(key)   # key를 회전
#                 for x in range(m):
#                     for y in range(m):
#                         new_lock[i+x][j+y] += r_key[x][y]    # new_lock에 기존 키 삽입

#                 # 자물쇠와 열쇠가 일치하는지 (전부 1인지 체크)
#                 if check(new_lock):
#                     return True
                
#                 # 자물쇠에서 열쇠 다시 빼기
#                 for x in range(m):
#                     for y in range(m):
#                         new_lock[i+x][j+y] -= r_key[x][y]
#     return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# ----------------------------------------------------------------------------
# rotation() 함수 개선
# ----------------------------------------------------------------------------
def rotation(array, d): # 회전 각도 d 1:90도, 2: 180도, 3: 270도
    n = len(array)  # 배열의 길이

    result = [[0] * n for _ in range(n)]

    # for i in range(n):
    #     for j in range(n):  # 결과 리스트
    #         result[j][n-i-1] = array[i][j]

    if d % 4 == 1:  # 90도 회전
        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = array[i][j]
    elif d % 4 == 2:
        for i in range(n):
            for j in range(n):
                result[n-i-1][n-j-1] = array[i][j]
    elif d % 4 == 3:
        for i in range(n):
            for j in range(n):
                result[n-j-1][i] = array[i][j]
    else:
        for i in range(n):
            for j in range(n):
                result[i][j] = array[i][j]
    return result

# 자물쇠 중간이 부분이 모두 1인지 체크
def check(new_lock):
    LockLength = len(new_lock)//3

    for i in range(LockLength, LockLength*2):
        for j in range(LockLength, LockLength*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n  = len(lock)
    m = len(key)

    # 자물쇠 크기를 기존의 3배로 불리기
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 열쇠 (1,1)부터 (n*2, n*2)까지 이동시키며 확인
    for i in range(1, n*2):
        for j in range(1, n*2):
            # 열쇠를 0, 90, 180, 270도록 회전
            for d in range(4):
                r_key = rotation(key, d)   # key를 회전
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += r_key[x][y]    # new_lock에 기존 키 삽입

                # 자물쇠와 열쇠가 일치하는지 (전부 1인지 체크)
                if check(new_lock):
                    return True
                
                # 자물쇠에서 열쇠 다시 빼기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= r_key[x][y]
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))