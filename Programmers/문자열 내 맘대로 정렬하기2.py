def solution(strings, n):
    answer = sorted(strings)
    print(answer)
    answer = sorted(answer, key=lambda x: x[n])

    return answer


print(solution(["abce", "abcd", "cdx"],2))