def solution(board, moves):
    def minus(x):
        return x-1
    moves=list(map(minus, moves))#[0, 4, 2, 4, 0, 1, 0, 3]
    # len(board)
    cnt=0
    stack=[]
    for j in  moves:
        if len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()#사라지기
            stack.pop()
            cnt+=2
        for i in range (len(board)):    
            if board[i][j] !=0:
                stack.append(board[i][j])#스택에 추가
                board[i][j]=0#뺀거니꺼 0으로 변경
                break
    return cnt            

# 약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.