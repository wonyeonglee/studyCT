def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    answer += phone_number[-4:]

    print(phone_number[-4:])
    return answer

print(solution("01033334444"))