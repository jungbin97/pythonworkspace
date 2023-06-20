# ----------------------------------------------------------------------------
# [programmers] 다리를지나는트럭 (queue, python)
# ----------------------------------------------------------------------------
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 대기트럭
    truck_stand = deque(truck_weights)
    # 다리위 트럭
    bridge = deque(0 for _ in range(bridge_length))
    # 경과 시간 초기화
    time = 0
    # 다리위 트럭 무게
    bridge_in_weight = 0

    while len(truck_stand) or bridge_in_weight > 0:
        # 대기트럭이 있거나 이동중인 트럭이 있는 동안 반복
        removedTruck = bridge.popleft()    # 다리에서 하나 제거
        bridge_in_weight -= removedTruck

        if len(truck_stand) and bridge_in_weight + truck_stand[0] <= weight:
            # 새 트럭이 다리에 올라갈 수 있다면
            newTruck = truck_stand.popleft()
            bridge.append(newTruck)
            bridge_in_weight += newTruck

        else:   # 새 트럭이 다리에 올라갈 수 없다면
            bridge.append(0)    # 오른쪽에 0을 삽입하여 다리 길이 유지

        time += 1
    return time

print(solution(100, 100, [10]))