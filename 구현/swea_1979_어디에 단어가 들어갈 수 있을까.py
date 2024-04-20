# ----------------------------------------------------------------------------
# D2[SWEA_1979] 어디에 단어가 들어갈 수 있을까 
# ----------------------------------------------------------------------------
for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    # 그래프
    graph = [list(input().split()) for _ in range(n)]

    count = 0

    def func(graph):
        global count
        for i in graph:
            tmp = "".join(i)
            tmp = tmp.split("0")
            print(tmp)
            for j in tmp:
                if len(j) == k:
                    count += 1

    func(graph)        
    func(zip(*graph))

    print(f"#{tc} {count}")


# 요약
# n퍼즐의 크기 k는 특정 단어의 길이
# k가 들어갈수 있는 자리수 개수를 출력하라. (크기는 딱 맞아야함)

# 풀이
# 0을 구분자로 사용하여 1의 크기 구하기


