def solution(numbers):
    import itertools
    answer = 0

    # new=list(map(int, numbers))#문자열을 하나씩 원소로 만들고 그 원소를 int로 
    new=list(numbers)
    def is_prime_number(num):
        if num==0 or num==1:
            return False
        else:
            for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
                if num%n == 0:
                    return False

            return True
    permutations_list=[]    
    for k in range(len(numbers)+1):
        for i in itertools.permutations(new,k+1):   
                permutations_list.append(''.join(i))


    permutations_list=list(map(int, permutations_list))#문자열 원소를 int로 변경
    ans=list(set(permutations_list))#중복제거
    for i in ans :
        if is_prime_number(i):
            answer+=1
    return answer        