#모험가 길드

n= int(input("모험가 수 : ")) # 모험가 명수를 입력받는다.
scare_point = [] #각 모험가 수 마다 공포도 배열

for i in range(n):
    scare_point.append(int(input("공포도 입력: "))) #공포도 입력받는다.
scare_point.sort(reverse=True) #작은수 만큼, 내림차림순으

sum =0
i=0 #인덱스  number
while(i<len(scare_point)):
    i=i+scare_point[i]
    sum+=1

print(sum)

