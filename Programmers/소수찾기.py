def solution(n):
    tflist = [True] *(n+1)

    for i in range(2, int(n**0.5 )+1):
        if(tflist[i] == True):#소수면 걔 배수들은 다 소수가 아니다
            for j in range(i*i,n+1, i):
                tflist[j] = False
    answer = [i for i in range(2,n+1) if tflist[i] == True]
    return answer


print(solution(10))
