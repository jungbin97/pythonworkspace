# ----------------------------------------------------------------------------
# [programmers] 완주하지 못한 선수 (hash)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#  정확성 테스트 : pass                효율성 테스트 : 1~5case nonpass(시간초과)
#  시간 복잡도 : O(N^2)
#  1. set()으로 중복 제거 후 완주하지 못한 사람 체크할 딕셔너리 생성
#  2. 참가자 중 완주자리스트에 있으면 완주자리스트에서 제거
#  3. 없으면 딕셔너리에 +1
#  4. 딕셔너리에서 value값이 1이면 반환
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
#  정확성 테스트 : pass                효율성 테스트 : 1~5case pass
#  1. 딕셔너리에 해쉬값을 키, 이름을 value로 초기화
#  2. 참가자 hash값 총합에서 완주자 hash값을 빼면 완주하지못한 사람 hash값만 남는다
#  4. 딕셔너리에 해당 해쉬값을 키로가지는 value 값 얻음
# ----------------------------------------------------------------------------
# def solution(participant, completion):
#     dic = dict()
#     hashSum = 0

#     for par in participant:
#         dic[hash(par)] = par
#         hashSum += hash(par)

#     for com in completion:
#         hashSum -= hash(com)

#     return dic[hashSum]

# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
# ----------------------------------------------------------------------------
#  다른 사람 풀이
#  시간 복잡도 : O(nm) => O(n)
#  Collections 모듈 Counter 클래스 사용 : 중복된 데이터가 있는 리스트를 각원소가 몇번 등장하는지 딕셔너리 형태로 반환
#  산술 연사자 사용 가능 : collections.Counter(participant) - collections.Counter(completion) => Counter({'mislav':1}) 반환 
# ----------------------------------------------------------------------------
import collections
def solution(participant, completion): 
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
