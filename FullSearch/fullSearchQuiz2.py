#완전탐색
#소수 찾기
#
#
from itertools import permutations


def check_sosu(number):  # 소수인지 check 하는 함수
    if(number<2):
        return False
    for i in range(2, number, 1):
        if (number % i == 0):  # i로 나누어지면
            return False
    return True


def solution(numbers):
    sosu_sum = []
    number_list = list(numbers)  # number 하나씩 쪼개서 리스트에
    for i in range(1, len(number_list) + 1, 1):  # 한자리부터 검사
        combinationlist = list(permutations(number_list, i))  # i개를 가지는 모든 조합 생성
        print(combinationlist)
        for com in combinationlist:  # 조합 검사
            com_number = ''
            for i in range(len(com)):
                com_number += com[i]
            com_number = int(com_number)
            if (not com_number in sosu_sum and(check_sosu(com_number)==True)):  # 소수 리스트에 없고 소수이
                sosu_sum.append(com_number)
    print(sosu_sum)
    return len(sosu_sum)

print(solution('011'))