#곱하기 혹은 더하기

s = list(map(int, input("숫자열 입력 : ")))
sum=0

for n in s:
    if(n==0 or sum==0):
        sum+=n
    else:
        sum = sum*n
print(sum)
