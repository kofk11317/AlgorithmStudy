from collections import deque#앞에가 먼저 나가야 하기 때문에 큐 활용해서 풀어봄

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    hap = 0
    dari = deque([0] * bridge_length)#앞뒤로 추가하거나 삭제해야하기 때문에 큐 사용
    truck_weights = deque(truck_weights) #앞에가 먼저 나가야 하기 때문에 큐 활용해서 풀어봄

    while truck_weights or hap > 0:
        hap -= dari.popleft()

        if truck_weights and hap + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            hap += truck
            dari.append(truck)
        else:
            dari.append(0)
        cnt += 1

    return cnt