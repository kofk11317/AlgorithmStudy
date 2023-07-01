def solution(array, commands):
    answer=[]
    for i in (commands):
            (start)=(i[0]-1)
            (end)=i[1]
            (select)=(i[2]-1)
            new=array[start:end]
            new.sort()

            answer.append(new[select])
    return answer        