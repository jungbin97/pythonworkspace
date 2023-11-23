def solution(today, terms, privacies):
    result = []
    today_year, today_month, today_day = map(int, today.split("."))
    today = today_year * 12 * 28 + today_month * 28 + today_day

    for iter, value in enumerate(privacies):
        personal_info_date, term = value.split(" ")
        year, month, day = map(int, personal_info_date.split("."))
        personal_info_date = year * 12 * 28 + month * 28 + day
        
        for t in terms:
            term_condition_type, expiration_period = t.split(" ")
            expiration_period = int(expiration_period) * 28

            if term == term_condition_type:
                personal_info_date += expiration_period
                    
        if today >= personal_info_date:
            result.append(iter+1)
    
    return result