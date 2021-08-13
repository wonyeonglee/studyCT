import re

def solution(new_id):
    #아이디 길이 3<= x<=15
    #알파벳 소문자, 숫자, -, _, . 만 사용가능
    #. 는 처음 끝 사용 불가, 연속 사용 불가
    #1단계 -> 모든 대문자를 소문자로  (lower)
    print("처음 문자열 : " + new_id)
    new_id = new_id.lower()
    print("1단계 통과 후  : " + new_id)
    #2단계
    text_reg = re.compile("[^a-z0-9-_.]")
    except_text =text_reg.findall(new_id) #제외한 문자들 찾고
    print(except_text)
    for w in except_text:
        new_id = new_id.replace(w,"")#삭제 해주기
    print("2단계 통과 후  : " + new_id)
    #3단계
    text_reg = re.compile("\.{2,}") #.이 두개이상인거
    except_text = text_reg.findall(new_id)
    print(except_text)
    for w in except_text:
        new_id = new_id.replace(w,".") #하나로 바꿔준다..
    print("3단계 통과 후  : " + new_id)
    #4단계
    if(new_id.startswith('.')):#처음이나 끝에 있다면 제거 -> 어케??...
        new_id = new_id[1:] #앞에거 잘라준다
    if(new_id.endswith('.')):
        new_id = new_id[ :-1] #뒤에거 잘라준다
    print("4단계 통과 후  : " + new_id)
    #5단계
    if(len(new_id) == 0):
        new_id = "a"
    print("5단계 통과 후  : " + new_id)
    #6단계
    if(len(new_id)>=16):
        new_id = new_id[:16]
        if(new_id.endswith('.')):
            new_id = new_id[ :-1]
    print("6단계 통과 후  : " + new_id)
    #7단계
    if(len(new_id)<=2):
        last_word = new_id[len(new_id)-1]
        while(len(new_id)<3):
            new_id +=last_word
    print("7단계 통과 후  : " + new_id)
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))