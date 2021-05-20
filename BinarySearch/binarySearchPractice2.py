#떡볶이 떡 만들기

num, requestLength = map(int, input("떡 개수, 요청길이 : ").split())
dducks = list(map(int, input("떡 길이").split()))
start = 0
end = max(dducks) #제일 큰 길이
result = 0
def binary_search(array,target,start,end):
    while(start<=end):
        sum = 0
        mid = int((start+end)//2)#중간길이
        #중간인덱스 길이로 잘랐을 때 손님이 가져갈 수 있는 총 길이를 구한다
        for dduck in array:
            if(dduck<=mid): #절단 길이보다 작거나 같으면 가져갈 수 있는 떡이 없다
                continue
            else: #절단 길이보다 크면 (원래 떡 길이 - 절단길이) 만큼 가져갈 수 있다.
                sum= sum+ (dduck-mid)
        if(sum>=target): #떡의 길이가 최소 요청보다 크거나 같으면
            result= mid
            start = mid+1
        else:
            end = start-1

        print(start,end,mid)
    return result

print(binary_search(sorted(dducks),requestLength,0,end))

