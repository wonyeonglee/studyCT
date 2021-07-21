#문자열 재정렬

numbers = ['0','1','2','3','4','5','6','7','8','9']
s = input() #문자열 입력받기
sorted_s = sorted(s)
numbers_sum = 0  #숫자 합 변수
new_s =''
for i in range(len(sorted_s)):
    if (sorted_s[i] in numbers):
        numbers_sum +=int(sorted_s[i])
    else:
        new_s += sorted_s[i]

new_s += str(numbers_sum)

print(new_s)

