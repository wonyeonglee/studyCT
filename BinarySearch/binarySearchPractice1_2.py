#부품 찾기- 다른 풀이

n = int(input("부품 개수: "))
materialNums = list(map(int, input("부품들 번호").split()))
m = int(input("요청 부품 번호: "))
requestNums = list(map(int, input("번호 :").split()))

for num in requestNums:
    if(num in materialNums):
        print("yes", end =" ")
    else:
        print("no", end =" ")