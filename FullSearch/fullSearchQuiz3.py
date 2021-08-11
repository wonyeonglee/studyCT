def solution(brown, yellow):
    capetsum = brown + yellow
    # 가로 * 세로 조합 수 (가로 >= 세로)
    combinationList = []
    answer = []
    # capetsum의 약수 구하기
    for i in range(1, capetsum + 1):  # (i가 가로)
        if (capetsum % i == 0):
            if (i >= (capetsum // i)):  # 가로가 더 길면
                combinationList.append((i, capetsum // i))  # 조합 추가
    print(combinationList)
    for com in combinationList:  # 조합 탐색
        if ((com[0] // 2) * (com[1] // 2) == yellow):
            answer.append(com[0])
            answer.append(com[1])

    return answer

print(solution(24,24))