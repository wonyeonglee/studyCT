#ATM (백준 알고리즘 문제)
n = int(input())
atmList = map(int,input().split())
sum=0
wholesum=0
atmList = sorted(atmList)
for i in range(len(atmList)):
    sum = sum+atmList[i]
    wholesum+=sum
print(wholesum)