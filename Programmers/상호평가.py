def solution(scores):
    answer = []
    score_of_allstud = [[0] * len(scores)] *len(scores)
    for i in range(len(scores)):  # i는 학생번호
        for j in range(len(scores)):
            score_of_allstud[j].append(scores[i][j]) # i가 준사람
            #j가 받은사람 score_of_all_stud[받은사]람[준사람]
    print(score_of_allstud)
    for i in range(len(score_of_allstud)):
        if(min(score_of_allstud[i])==score_of_allstud[i][i] or max(score_of_allstud[i])==score_of_allstud[i][i]):
        #최고점이나 최저점이 자기가 평가한 점수라면
            average = sum(score_of_allstud[i])-score_of_allstud[i][i]/(len(scores)-1)
        #자기 점수 빼고 평균 구하
        else:
            average = sum(score_of_allstud[i])/len(scores)
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


    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))