def solution(sizes):
    #가로세로 상관말기
    #모아놓기?
    width = []
    height = []
    answer = 0
     # 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다.
        # 가장 작은 지갑을 만들 때
    n=len(sizes)
    for i in range (n):
        #항마다 큰값과 작은값이 있을텐데 
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
        # 큰거는 가로 배열로 작은거는 세로배열로
        # width.sort(reverse=True) 속도가 차이 많이남
        # height.sort(reverse=True)
    answer=max(width)*max(height)
    return answer