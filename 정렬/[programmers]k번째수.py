# -------------------------------------------------------------------------
#  [programmers] k번째수 (정렬)
#  1. 리스트 슬라이싱으로 i, k 범위로 슬라이싱
#  2. 정렬 후, k 번째 수 추출
#  3. 추출한 요소 리스트에 추가해줌
# -------------------------------------------------------------------------
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(tmp[commands[i][2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))