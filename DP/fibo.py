# 동적 프로그래밍으로 구현한 피보니치
# memo를 위한 리스트를 생성하고.
# momo[0]을 0 memo[1] 1로 초기화 한다.


#recursive 방식
# def fibo1(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo1(n-1) + fibo1(n-2))
#     return memo[n]

# memo = [0, 1]

# fibo1(5)
# print(memo)

# iterative 방식
def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

fibo2(5)
print()