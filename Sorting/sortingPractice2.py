#성적이 낮은 순서로 학생 출력하기

n = int(input("학생 수 : ")) #학생 수 입력받기
def keys(data):
    return data[1]
info = []
for i in range(n):
    input_data = input("학생 이름, 점수").split() #정보 입력받기
    info.append((input_data[0],int(input_data[1]))) #튜플 형식으로 리스트에 넣기

info =sorted(info,key=keys) #점수기준으로 정렬하기

for i in info: #점수 낮은 순으로 이름 출력하기
    print(i[0], end=" ")