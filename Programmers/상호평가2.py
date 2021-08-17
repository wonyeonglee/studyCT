def solution(scores):
    score = list(map(list, zip(*scores))) #transpose
    answer = ''
    for i, numberlist in enumerate(score):
        if(max(numberlist) == numberlist[i] and numberlist.count(max(numberlist))==1 ): #최대
            average = (sum(numberlist) - max(numberlist))/ (len(scores)-1)
        elif(min(numberlist) == numberlist[i] and numberlist.count(min(numberlist))==1 ):
            average = (sum(numberlist) - min(numberlist))/ (len(scores)-1)
        else:
            average = sum(numberlist)/len(scores)


        if(average >=90):
            answer+='A'
        elif(average>=80):
            answer+='B'
        elif(average>=70):
            answer+='C'
        elif(average>=50):
            answer+='D'
        else:
            answer+='F'
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))