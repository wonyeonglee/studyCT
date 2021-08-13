def solution(nums):
    can_get_num = len(nums)//2 #가져갈 수 있는 폰켓몬 수
    n=len(set(nums))
    resultsum = 1
    for i in range(can_get_num):
        resultsum *= n
        n -=1
    return resultsum//2

print(solution([3,1,2,3]))