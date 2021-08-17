def solution(arr):
    ex_num = arr[0]
    answer = [ex_num]
    for i in range(1, len(arr)):
        if (ex_num != arr[i]):  # 이전 숫자와 다르면
            answer.append(arr[i])
            ex_num = arr[i]

    return answer

print(solution([1,1,3,3,0,1,1]))