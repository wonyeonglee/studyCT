def solution(strings, n):
    answer = sorted(strings, key = lambda x : x[n])
    result = []
    string = [ w[n] for w in answer]
    i=0
    while(i<=len(string)-1):
        if(string.count(string[i])==1):
            i=i+1
        else: # 같은 문자가 여러개 일 ㄸ ㅔ
            countNumber = string.count(string[i])
            answer[i:i+countNumber] = sorted(answer[i:i+countNumber])
            i=i+countNumber
    return answer

print(solution(["abce", "abcd", "cdx"],2))


