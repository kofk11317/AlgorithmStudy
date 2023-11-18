def solution(s):
    cnt=0
    noncnt=0
    answer=0
    x=s[0]
    for i in range (len(s)):
    
        if s[i]==x:
            cnt+=1
        else:
            noncnt+=1
        if cnt==noncnt:
            answer+=1
            cnt=0
            noncnt=0
            try:            
                x=s[i+1]  # 다음 요소를 확인

            except IndexError:  # 인덱스 에러가 발생하면
                break
    if cnt!=noncnt:
        answer+=1
        
    return answer        