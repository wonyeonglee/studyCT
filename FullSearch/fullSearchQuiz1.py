#완전 탐색
#프로그래머스 모의고사 1
#모의고사

def solution(answers):
    answer_sums = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):  # 문제 답 check
        if (one[i % len(one)] == answers[i]):  # 1번 수포자가 정답인경우
            answer_sums[0] += 1  # 정답 수 증가
        if (two[i % len(two)] == answers[i]):  # 2번 수포자가 정답인 경우
            answer_sums[1] += 1  # 정답 수 증가
        if (three[i % len(three)] == answers[i]):  # 3번 수포자가 정답인 경우
            answer_sums[2] += 1
    # 최종적으로 제일 많이 맞힌 수포자 배열 출력
    max_sum = max(answer_sums)  # 제일 많이 맞힌 개수
    answer = []
    if (answer_sums[0] == max_sum):  # 1번이 가장많이 맞혔다
        answer.append(1)
    if (answer_sums[1] == max_sum):  # 2번이 가장많이 맞혔다
        answer.append(2)
    if (answer_sums[2] == max_sum):  # 3번이 가장많이 맞혔다
        answer.append(3)

    return answer