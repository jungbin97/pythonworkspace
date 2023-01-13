T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())    # N 카드 갯수
    ai = list(map(int, input()))
    
    cards = [0 for i in range(10)]
    result = 0
    max = 0

    for i in ai:
        cards[i] += 1
    
    for i, count in enumerate(cards):
        if count >= max:
            max = count
            result = i

    print("#%d %d %d" %(test_case, result, max))

