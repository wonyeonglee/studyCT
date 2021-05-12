#거스름돈 문제

changes = [500,100,50,10]
N = int(input())
coin_sum = 0

for change in changes:
    if(N>=change):
        coin_sum += N//change
        N = N % change
print(coin_sum)