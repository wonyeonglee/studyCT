#1이 될 때까지

n, k = map(int, input("값 입력: ").split())
sum=0
while(n != 1):
    while(n % k !=0):
        n-=1
    n//= k
    sum+=1
print(sum)