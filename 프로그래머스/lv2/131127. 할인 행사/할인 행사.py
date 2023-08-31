def solution(want, number, discount):
    
    from collections import Counter

    result=0
    cnt=dict(zip(want,number))
    length=len(discount)


    for i in range (length):
        new=(discount[i:i+10])
        frequency_dict = dict(Counter(new)) # 리스트를 딕셔너리로 바꾸는법
        if cnt==frequency_dict:
            result+=1
    return result
# 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.
 # 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다.
    # 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.