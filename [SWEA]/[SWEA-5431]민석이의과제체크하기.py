# ----------------------------------------------------------------------------
#  1. 전체 학생 리스트를 생성
#  2. 과제를 제출한 번호 리스트입력받아 해당 번호 학생 True로 변경
#  3. 전체 학생 리스트에 False에 해당하는 학생 번호 출력
#  시간 복잡도 : O(n)
# ----------------------------------------------------------------------------

for test_case in range(1, int(input())+1):
    # 수강생 수 : N, 과제를 제출한 사람 수 : K
    N, K = map(int, input().split())

    # 전체 학생 리스트
    totalList = [False for _ in range(1,N+1)]
    
    # 과제를 제출한 번호 리스트
    submitList = list(map(int, input().split()))
    
    for i in submitList:
        if totalList[i-1] == False:
            totalList[i-1] = True
    
    nonSumitList = []
    for i, j in enumerate(totalList):
        if j == False:
            nonSumitList.append(i+1)
    
    result = " ".join(map(str, nonSumitList))
    print("#%d %s" %(test_case, result))
