import math

def solution(progresses, speeds):
    answer = []
    # 개발은 뒤에 있는게 먼저 될 수 있지만 배포는 앞에 기능이 배포될 때 같이 된다.
    # 배포 되어야 하는 순서 progresses
    days = []
    result_sum = 0
    ex_day = 10000
    for i in range(len(progresses)): #i==0
        day = math.ceil((100 - progresses[i]) / speeds[i]) #걸리는 데이 20
        print(i, day)
        if(i==0):
            result_sum +=1
            ex_day = day #10
            continue
        if(i==len(progresses)-1):
            result_sum+=1
            answer.append(result_sum)
        if (day <= ex_day):
            result_sum+=1
        else:
            answer.append(result_sum)
            result_sum = 1
            ex_day = day

        #ex_day = math.ceil((100 - progresses[i]) / speeds[i])


#[5,10,1,1,20,1]  #0번째 인덱스 --> 5 pop
    #2번째 인덱스 10 --> pop
    print(days)

    return answer
print(solution([93, 30, 55],[1, 30, 5]))