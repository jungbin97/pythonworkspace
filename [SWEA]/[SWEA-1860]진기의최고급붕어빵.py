# ----------------------------------------------------------------------------
#  1. 사람의 들어오는 순서가 일정하지 않으므로 정렬
#  2. 들어온 시간//M * K 해당 사람이 들어온 시간동안 만들수 있는 빵의 개수를 만든다.
#  3. 이후 몇 번째 사람인지 체크후 만들 수 있는 빵보다 온사람수가 크면 Impossible 반환
# ----------------------------------------------------------------------------
impossible = "Impossible"
possible = "Possible"

def solution(N, M, K, people):
    # 순서 정렬
    people.sort()
    
    # 붕어빵 개수 계산
    for i in range(N):
        total = (people[i]//M)*K
        if total < i + 1:
            return impossible
        return possible    


for test_case in range(1, int(input())+1):

    # N : 자격을 얻은 사람 수, M : 들인 시간 초, K : 만들어진 붕어빵 개수
    N, M, K = map(int, input().split())

    # 도착하는 사람 초 단위
    people = list(map(int, input().split()))

    answer = solution(N, M, K, people)
    print("#{} {}".format(test_case, answer))