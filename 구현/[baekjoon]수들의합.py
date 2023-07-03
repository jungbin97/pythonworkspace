# ----------------------------------------------------------------------------
# [baekjoon]수들의합4 (투포인터, python)
# ----------------------------------------------------------------------------
n = int(input())

startPoint = 1
endPoint = 1
count = 1
sum = 1

while(endPoint != n):
    if sum == n:    # count 증가, endPoint증가, sum + endPoint
        count += 1
        endPoint += 1
        sum = sum+endPoint
    elif sum>n:     # sum-startPoint, startPoint증가
        sum = sum-startPoint
        startPoint += 1
    elif sum<n:     # endPoint증가, sum+endPoint
        endPoint += 1
        sum = sum+endPoint

print(count)
