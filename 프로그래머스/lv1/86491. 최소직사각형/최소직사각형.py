def solution(sizes):
    #가로세로 상관말기
    #모아놓기?
    width = []
    height = []
    answer = 0
    
    n=len(sizes)
    for i in range (n):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    answer=max(width)*max(height)
    return answer