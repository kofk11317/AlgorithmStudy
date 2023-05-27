# from collections import deque
from heapq import heappop, heappush, heapify

def solution(scoville, K):
    cnt = 0

    # 최소힙 구조로 변환
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            cnt = -1
            break
        new1 = heappop(scoville)
        new2 = heappop(scoville)
        heappush(scoville, new1 + (new2 * 2))
        cnt += 1
    return cnt    
#     cnt=0
#     scoville.sort()
#     while True:
#         scoville=deque(scoville)
#         new1=scoville.popleft()
#         new2=scoville.popleft()
#         scoville.append(new1+(new2*2))
#         scoville=list(scoville)
#         scoville.sort()
#         cnt+=1
#         if scoville[0]>=K:#애초에 정렬이 되어있기 때문에 min함수 쓸 필요가 없음
#             break
#     return cnt        
# # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)