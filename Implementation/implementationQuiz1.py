#럭키 스트레이트

n = input() #점수 입력받기
left_sum = 0
right_sum = 0
for i in range(len(n)):
    if(i<len(n)//2): #반 나눠서 앞자리 더하기
        left_sum += int(n[i])
    else:
        right_sum += int(n[i])

if(left_sum == right_sum):
    print('LUCKY')
else:
    print('READY')
