import re


def solution(s):
    word = [("zero", "0"), ("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"),
            ("seven", "7"), ("eight", "8"), ("nine", "9")]
    alphabet_regex = re.compile("[a-z]")
    if (len(alphabet_regex.findall(s)) == 0):  # 영어가 없는 경우
        return int(s)
    else:
        for pair in word:
            if (pair[0] in s):
                print(pair[0])
                print(pair[1])
                s.replace(pair[0], pair[1])

    return int(s)

print(solution("one4seveneight"))