# ----------------------------------------------------------------------------
# D3[swea_1216] 회문2
# ----------------------------------------------------------------------------
# for _ in range(10):
#     tc = int(input())
#
#     graph = [list(input()) for _ in range(100)]
#     graph_transpose = list(map(list, zip(*graph)))
#
#     answer = 1
#     for i in range(100):
#         for j in range(100):
#             for k in range(100):
#                 if j+k < 100:
#                     word1 = graph[i][j:j+k]
#                     word2 = graph_transpose[i][j:j+k]
#                     if word1 == word1[::-1]:
#                         answer = max(answer, len(word1))
#                     if word2 == word2[::-1]:
#                         answer = max(answer, len(word2))
#
#     print(f"#{tc} {answer}")

for _ in range(10):
    tc = int(input())

    graph = [list(input()) for _ in range(100)]
    graph_transpose = list(map(list, zip(*graph)))

    def is_pal(graph, length):
        for lst in graph:
            for i in range(100-length+1):
                for j in range(length//2):
                    if lst[i+j]!= lst[i+length-1-j]:
                        break
                else:
                    return True
        return False

    for length in range(100, 1, -1):
        if is_pal(graph, length) or is_pal(graph_transpose, length):
            break
    print(f"#{tc} {length}")

# 풀이
# 문자열 전체를 비교하지말고, 인덱스로 다른 글자 나오면 바로 False반환하게 하여 최적화 가능하다.