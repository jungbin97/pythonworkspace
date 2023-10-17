n, k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
ans = 0

while True:
    if cnt > k:
        if arr[start] % 2 == 1:
            cnt -= 1
        start += 1
    elif end == n:
        break
    else:
        if arr[end] % 2 == 1:
            cnt += 1
        end += 1
    if cnt <= k:
        ans = max(ans, end - start - cnt)

print(ans)
