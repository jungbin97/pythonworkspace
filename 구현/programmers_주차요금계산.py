from collections import defaultdict
import math

def solution(fees, records):
    answer = []

    dic = {}
    total = defaultdict(int)
    
    default_time, default_fee, unit_time, unit_fee = fees
    for record in records:
        time, car_number, entry_exit_detail = record.split()
        # 시간, 분 => 분으로 변환
        h, m = map(int, time.split(":"))
        time = (h*60) + m
        
        # 입차기록
        if entry_exit_detail == "IN":
            dic[car_number] = time
        elif entry_exit_detail == "OUT":
            total[car_number] += time - dic[car_number]
            # 이요한 IN 제거
            del dic[car_number]

    # dic에 남으면 출차를 안한 차임
    for car_number, time in dic.items():
        # 23:59 => 1439분임
        total[car_number] += (1439 - time)

    for key, value in total.items():
        result = default_fee
        if value > default_time:
            result += math.ceil((value - default_time)/unit_time)*unit_fee
        answer.append((key, result))
    
    answer.sort()

    return [i[1] for i in answer]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))