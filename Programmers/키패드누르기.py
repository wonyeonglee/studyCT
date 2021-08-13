def solution(numbers, hand):
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    left_position = (3, 0)  # 처음 왼손 엄지의 위치 * 자리
    right_position = (3, 2)  # 지금 오른손 엄지의 위치
    phone_map = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    answer = ""
    for n in numbers:
        if (n in left_number):  # 1,4,7에 해당하면 왼손 엄지 사용
            answer += "L"
            left_position = phone_map[n]  # 왼손 엄지 위치 바꾸기
        elif (n in right_number):  # 3,6,9에 해당하면 오른속 엄지 사용
            answer += "R"
            right_position = phone_map[n]  # 오른손 엄지 위치 바꾸기
        else:
            # 거리 비교하기
            # 왼손 엄지로 갈 경우 이동 거리 구하기
            # 0번째 - 0번째
            left_distance = abs(left_position[0] - phone_map[n][0]) + abs(left_position[1] - phone_map[n][1])
            right_distance = abs(right_position[0] - phone_map[n][0]) + abs(right_position[1] - phone_map[n][1])
            if (left_distance == right_distance):  # 만약 거리가 같으면
                if (hand == "left"):  # 왼손잡이면 왼손으로이동
                    answer += "L"
                    left_position = phone_map[n]  # 왼손 엄지 위치 바꾸기
                else:
                    answer += "R"
                    right_position = phone_map[n]  # 오른손 엄지 위치 바꾸기
            elif (left_distance < right_distance):
                answer += "L"
                left_position = phone_map[n]  # 왼손 엄지 위치 바꾸기
            else:
                answer += "R"
                right_position = phone_map[n]  # 오른손 엄지 위치 바꾸기
        print(answer)
        print(left_position)
        print(right_position)
        print("----------")

    return answer
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))