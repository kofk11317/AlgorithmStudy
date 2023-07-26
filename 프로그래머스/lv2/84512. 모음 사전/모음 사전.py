def solution(word):
    import itertools
    product_list=[]
    new=['A', 'E', 'I', 'O', 'U']

    for k in range(5): # 첨부터 끝까지 한자리수 두자리수 ... n자리수 까지 확인
            for i in itertools.product(new,repeat=k+1):   
                    product_list.append(''.join(i))
           
    answer =sorted(product_list).index(word)+1 
    return answer