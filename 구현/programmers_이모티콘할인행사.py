# ----------------------------------------------------------------------------
# [programmers] 이모티콘 할인행사(구현) 
# ----------------------------------------------------------------------------
# from itertools import combinations_with_replacement
from itertools import product

def solution(users, emoticons):
    answer = []
    emo_len = len(emoticons)

    discount = [10, 20, 30, 40]

    # 중복 순열로 할인율 모두 확인 
    discount_case = list(product(discount, repeat= emo_len))  #예) discount = [10, 20] 이면 [(10, 10), (10, 20), (20, 10), (20, 20)]
    # discount_case = list(combinations_with_replacement(discount, emo_len))    # [(10, 10), (10, 20), (20, 20)]
    for case in discount_case:
        emo_plus_cnt = 0
        emo_sale_price = 0
        
        prices = []
        # 할인율 가격 반영
        for i in range(emo_len):
            # prices.append(int(emoticons[i] - (emoticons[i]*case[i]/100)))
            prices.append((emoticons[i] // 100) * (100 - case[i]))
            
        for percent_limit, emo_plus_limit in users:
            total_price=0
            for i in range(emo_len):
                # 퍼센트 제한보다 크면 가격 이모티콘 구매 비용에 반영
                if case[i] >= percent_limit:
                    total_price += prices[i]
                    
            if total_price >= emo_plus_limit:
                emo_plus_cnt += 1
            else:
                emo_sale_price += total_price
        answer.append((emo_plus_cnt, emo_sale_price))

    # 내림차순
    answer.sort(key=lambda x: (-x[0], -x[1]))
    print(answer[0])