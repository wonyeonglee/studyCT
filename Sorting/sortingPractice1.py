#위에서 아래로

n = int(input("수의 개수"))
array = [] #배열
for i in range(n):
    array.append(int(input()))
    array.sort()
array.reverse() #내림차순으로 정렬 
#수열 공백 구분으로 출력
for num in array:
    print(num, end=" ")
