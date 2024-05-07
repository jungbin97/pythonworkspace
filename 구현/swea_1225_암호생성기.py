# ----------------------------------------------------------------------------
# [swea_1225] 암호생성기
# ----------------------------------------------------------------------------
for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    
    reduce_value = 0
    while True:
        now = arr.pop(0)
        reduce_value += 1
        if 0 < now-reduce_value:
            arr.append(now-reduce_value)
            if reduce_value == 5:
                reduce_value = 0
        else:
            arr.append(0)
            break

    print(f"#{tc}", end=" ")
    print(*arr)

# 요약
# 값 8개가 주어지고, 1 감소하고 맨뒤로이동, 2 감소하고 맨뒤로이동.. 반복
# 0보다 작거나 같압지는 경우 0으로 유지하고, 프로그램 종료


# 풀이
# 5번 감소 시키는게 1사이클이다.