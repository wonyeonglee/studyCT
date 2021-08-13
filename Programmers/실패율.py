def solution(N, stages):
    # 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    answer = []
    stages = sorted(stages) #순서대로 정렬
    for i in range(1,N+1):
        #(단계, 실패율)
        if(i in stages):
            index = stages.index(i) #i단계가 젤 처음으로 나오는 인덱스 구하기
            fail =  stages.count(i)/(len(stages)-index) #실패ㅇ
        else:
            fail = 0
        answer.append((i, fail))
    answer = sorted(answer,reverse=True,key = lambda x:x[1])
    print(answer)
    result = [x[0] for x in answer]

    return result
print(solution(4,[4,4,4,4,4]))

#위의 방법은 너무 오래 걸린다..
#짧게 걸리는 방법을 -> 나중에 해보자