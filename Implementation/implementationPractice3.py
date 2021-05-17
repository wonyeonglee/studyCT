#왕실의 나이트

inputdata = input("처음위치")
x = int(ord(inputdata[0])) - (int(ord('a')-1))
y = int(inputdata[1])

sum=0
directions = [(2,1),(-2,1),(-2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] #이동할 수 있는 경우의 수 8가지
for direction in directions:
    if(x+direction[0]>=1 and x+direction[0]<=8 and y+direction[1]>=1 and y+direction[1]<=8):
        sum+=1

print(sum)

