import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
i = 0     # start Point
j = n-1   # end Point
count = 0
while(i < j):
    if arr[i]+arr[j] == m:
        count+=1
        j-=1
        i+=1
    elif arr[i]+arr[j]>m:
        j-=1
    elif arr[i]+arr[j]<m:
        i+=1
        
print(count)