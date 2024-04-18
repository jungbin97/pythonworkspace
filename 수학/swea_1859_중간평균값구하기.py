# ----------------------------------------------------------------------------
# D2[SWEA_1859] 중간 평균 값 구하기
# ----------------------------------------------------------------------------
# import sys
# input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    
    nums.remove(max(nums))
    nums.remove(min(nums))
    
    result = sum(nums)/len(nums)

    print("#{} {}".format(i, round(result)))

print((3 + 17 + 39 + 8 + 41 + 2 + 32 + 2)/8)
# 요약
# 10개의 수를 입력받아, 최대 수와 최소 수를 제외한 평균값을 출력하는 프로그램을작성하라(소숫점 첫째자리에 반올림)
# 최대 수와 최소 수가 중복되면?? => 같은 수 모두 빼야한다?

# 풀이
# 파이썬은 소수점 int() 형 변환시 소숫점자리를 버린다. 따라서 해당 문제는 round()로 반올림 해줘야한다.