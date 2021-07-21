#무지의 먹방 ㄹ ㅏ이브
#https://programmers.co.kr/learn/courses/30/lessons/42891

food_times = [3,1,2]
k = 5
index=0
if(sum(food_times)<=k):
    return -1
remind = k%len(food_times) #나머
mok = k//len(food_times) #지몫
#몫보다 작은 애들 찾는다.
for i in range(1,mok):
    if( i in food_times):
        remind +=food_times.count(i)
remind+=1

print(remind)


