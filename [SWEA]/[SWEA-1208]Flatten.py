# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# for test_case in range(1, 11):
#     # 덤프 횟수
#     dump = int(input())
#     count = 0
#     boxs = list(map(int, input().split()))
#     # 박스 높이 내림차순 정렬
#     boxs.sort(reverse=True)
    
#     for j in range(dump):
#         # 가장 큰 높이
#         boxs[0] -= 1
#         # 가장 작은 높이
#         boxs[len(boxs)-1] += 1
#         count += 1
#         boxs.sort(reverse=True)
        
#     print("#{} {}".format(test_case, max(boxs)-min(boxs)))
    
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
for test_case in range(1, 11):
    N = int(input())
    boxs = list(map(int, input().split()))

    for i in range(N):
        max_num = max(boxs)
        min_num = min(boxs)
        index_max_num = boxs.index(max_num)
        index_min_num = boxs.index(min_num)
        boxs[index_max_num] -= 1
        boxs[index_min_num] += 1

    print("# {} {}".format(test_case, max(boxs)-min(boxs)))