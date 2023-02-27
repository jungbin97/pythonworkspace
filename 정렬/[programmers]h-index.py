def solution(citations):
    answer = 0
    citations.sort()    # 오름차순 정렬
    h2 = []

    for i in range(len(citations)):
        h2.append(len(citations) - i)
        if citations[i] == h2[i]:
            answer = h2[i]
            return answer
    return answer

print(solution([3, 0, 6, 1, 5]))
# --------------- testcase 1개 통과 ---------------
# ------------------------------------------------
def solution(citations):
    citations.sort()    # 오름차순 정렬

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
        
    return 0