#설탕 배달 (백준 문제)

n = int(input())
sum=0
original_n = n
#먼저 5킬로 먼저 담는다.
sum+= n//5
n = n%5
#그 다음 3킬로 담는다
sum+= n//3
n = n%3


if(n!=0):
    n= original_n
    sum = n // 3
    n = n%3
    if(n!=0):
        sum = -1

print(sum)




