from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 0
    sum_weights = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while truck_weights or sum_weights > 0:
        sum_weights -= bridge.popleft()

        if truck_weights and sum_weights + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            sum_weights += truck
            bridge.append(truck)
        else:
            bridge.append(0)
        sec += 1

    return sec