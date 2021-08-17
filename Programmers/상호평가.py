def solution(scores):
    answer = []
    scoresOfJ= [0] * len(scores)
    max_score = [(-1,0)] * len(scores)
    min_score = [(10000000,0)] * len(scores)
    for i in range(len(scores)):  # i번 학생 (점수 주는 사람)
        for j in range(len(scores)):  # j번 학생 (점수 받는 사람)
            scoresOfJ[j] += scores[i][j]
            if(max_score[j][0] <= scores[i][j]): #최대 점수
                if(max_score[j][0] == scores[i][j]):
                    same_sum = max_score[j][1] +1
                else:
                    same_sum = 0
                max_score[j] = (scores[i][j],same_sum)
            if(min_score[j][0] >= scores[i][j]):
                if(min_score[j][0] == scores[i][j]):
                    same_sum = min_score[j][1] +1
                else:
                    same_sum = 0
                min_score[j] = (scores[i][j],same_sum)
    for i in range(len(scoresOfJ)):
        if(max_score[i][0] ==scores[i][i] and max_score[i][1] == 0):#j가 받은 최대 점수가 j가 준거라
        #최고점이나 최저점이 자기가 평가한 점수라면
        # 만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.
            average = (scoresOfJ[i]-max_score[i][0])/(len(scores)-1)
        elif(min_score[i][0] == scores[i][i] and min_score[i][1] == 0):
            average = (scoresOfJ[i] - min_score[i][0]) / (len(scores) - 1)
        #자기 점수 빼고 평균 구하
        else:
            average = scoresOfJ[i]/len(scores)
        if(average>=90):
            answer.append("A")
        elif(average>=80):
            answer.append("B")
        elif(average>=70):
            answer.append("C")
        elif(average>=50):
            answer.append("D")
        else:
            answer.append("F")


    return ''.join(answer)
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))