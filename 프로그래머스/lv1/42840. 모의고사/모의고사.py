def solution(answers):
    result = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2= 0
    score3=0
    for i, answer in enumerate(answers):
        if one[i%5] == answer:
            score1 += 1
        if two[i%8] == answer:
            score2 += 1
        if three[i%10] == answer:
            score3 += 1
    Max=max(score1,score2,score3)
        #가장 높은 점수와 그 점수와 같은 수준으로 맞은 애를 찾았을때 결과에 append해줌
    if Max == score1:
        result.append(1)
    if Max == score2:
        result.append(2)
    if Max == score3:
        result.append(3)    
            

    return result