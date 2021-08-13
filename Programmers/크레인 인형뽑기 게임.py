def solution(board, moves):
    answer = 0
    #크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
    basket = []
    for move in moves: #크레인을 처음부터 움직이자
        for i in range(len(board)):
            if(board[i][move-1] != 0):#맨위에 인형이 있으면
                #바구니 넣기 전 마지막 원소와 비교
                if(len(basket)!=0 and basket[-1] == board[i][move-1]):#바구니에 넣을려는 것과 맨위에 있는 것과 같으면
                    basket.pop() #제거
                    answer+=2
                else:
                    basket.append(board[i][move-1])#바구니에 넣는다.
                board[i][move-1] = 0 #보드에서 인형 뺀다.
                break
        print(basket)
        print("-------")
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))