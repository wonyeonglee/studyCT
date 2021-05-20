#부품 찾기

n = int(input("부품 개수: "))
materialNums = list(map(int, input("부품들 번호").split()))
m = int(input("요청 부품 번호: "))
requestNums = list(map(int, input("번호 :").split()))

def binary_search(array,target,start,end):
    while(start<=end):
        mid = ((start+end)//2) #중간 인덱스 구하기
        if(array[mid]==target): #target을 찾으면 yes출력
            return "yes"
        elif(target<array[mid]): #target이 mid보다 작으면
            end = mid-1 #끝점의 인덱스를 change
        else: #target이 mid보다 크면
            start = mid+1 #시작점의 인덱스를 change
    return "no"

for num in requestNums:
    print(binary_search(sorted(materialNums),num,0,len(materialNums)), end=" ")

