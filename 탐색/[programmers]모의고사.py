# -------------------------------------------------
# [programmers] 모의고사 (완전탐색)
# -------------------------------------------------
def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    peoples = [0]*3
    result = []

    for idx, answer in enumerate(answers):
        if answer == a1[idx%len(a1)]:
            peoples[0] += 1
        if answer == a2[idx%len(a2)]:
            peoples[1] += 1
        if answer == a3[idx%len(a3)]:
            peoples[2] += 1

    for idx, s in enumerate(peoples):
        if s == max(peoples):
            result.append(idx+1)

    return result

print(solution([1,2,3,4,5]))