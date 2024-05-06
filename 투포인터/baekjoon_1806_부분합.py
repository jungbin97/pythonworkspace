# ----------------------------------------------------------------------------
# [baekjoon_1806] 부분합 
# ----------------------------------------------------------------------------
# N개의 길이 문자열 주어짐, S는 합의 크기
n, s = map(int, input().split())

string = list(map(int, input().split()))

start = 0
end = 0
INF = 1e9
interval_sum = string[0]

result = INF

while start <= end:
    # S보다 크거나 같으면
    if interval_sum >= s:
        result = min(result, end - start + 1)
        interval_sum -= string[start]
        start += 1
    else:
        end += 1
        if end < n:
            interval_sum += string[end]
        else:
            break

if result == INF:
    print(0)
else:
    print(result)
# 요약
# 10000이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 연속된 수들의 부분합중 합이 S이상되는것 중, 가장 짧은 길이를 구하여라

# 풀이
# S이상되는 합 중 가장 짧은 것을 구하려면, 큰수 끼리 붙어있어야?
# start, end