# ----------------------------------------------------------------------------
# [programmers] 완주하지 못한 선수 (hash)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#  정확성 테스트 : pass                효율성 테스트 : 1~5case nonpass(시간초과)
#  시간 복잡도 : O(N^2)
# ----------------------------------------------------------------------------
# def solution(participant, completion):
#     nonCompletion = dict()
#     for player in set(participant): 
#         nonCompletion[player] = 0

#     for player in participant :
#         if (player not in completion) : 
#             nonCompletion[player] += 1
#         else : completion.remove(player)

#     answer = "".join([k*v for k,v in nonCompletion.items()])
#     return answer
# ----------------------------------------------------------------------------
#  시간복잡도 : O(N+M) -> O(N)
# ----------------------------------------------------------------------------
def solution(participant, completion):
    dic = dict()
    hashSum = 0

    for par in participant:
        dic[hash(par)] = par
        hashSum += hash(par)

    for com in completion:
        hashSum -= hash(com)

    return dic[hashSum]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))