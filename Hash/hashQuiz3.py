from itertools import combinations

def solution(clothes):
    clothes_dic = {}
    one_sum = 0
    combinations_sum = 1
    for cloth in clothes:
        if (cloth[1] in clothes_dic):  # 이미 딕셔너리에 있는 종류이면
            clothes_dic[cloth[1]] += 1
        else:
            clothes_dic[cloth[1]] = 1
    key_combinations = []

    for i in range(1, len(clothes_dic.keys()) + 1):  # 키 별로 조합 만들기
        key_combinations.append(list(combinations((clothes_dic.keys()),i)))
    answer=0
    for comb in key_combinations:
        for j in range(len(comb)):
            tmp_sum = 1
            for i in range(len(comb[j])):
                tmp_sum *= clothes_dic[comb[j][i]]
            answer +=tmp_sum
    return answer

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))