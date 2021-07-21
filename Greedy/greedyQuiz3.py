#문자열 뒤집기 (적은 숫자를 바꾸는 걸로)
splitnumber = '0'
exchangenumber= '1'
s = input() #문자열 입력받기

if(s.count('1')<s.count('0')): # 1이 개수가 더 적으면
    splitnumber = '1'
    exchangenumber='0'
#문자열을 리스트로
s = list(s)
sum=0 #최초 횟수는 0으로 초기화

for i in range(len(s)):
    if(s[i]==splitnumber):
        s[i] = exchangenumber
        if(s[i+1]==splitnumber):
            continue
        else:
            sum+=1

print(sum)
