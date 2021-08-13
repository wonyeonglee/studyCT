def solution(phone_book):
    # 제일 길이가 짧은 거로 sorting -> 가능?
    phone_book = sorted(phone_book, key=lambda x: len(x))
    print(phone_book)
    for i in range(len(phone_book)-1):
        if(len(phone_book[i])<=len(phone_book[i+1])):
            for j in range(i + 1, len(phone_book)):
                print(j)
                print(phone_book[i],phone_book[j])
                if (phone_book[i] in phone_book[j]):
                    return False

    # 하나라도 접두어가 있으면 return False
    return True

print(solution(["12","123","1235","567","88"]))