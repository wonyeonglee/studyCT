def solution(w,h):
    #w와 h의 최대공약수
    n = w*h
    maxprime = 1
    for i in range(2,min(w,h)-1):
        if(w%i==0 and h%i==0):
            maxprime = i
    w = w//maxprime #최대 공약수로 나눈 나머지
    h = h//maxprime #최대 공약수로 나눈 나머지
    square_sum =0
    for i in range(1,w):
        square_sum += (h * i)//w #패턴 안에 사각형 수 2
    square_sum = square_sum*2
    not_sqare_in_pattern = (w*h - square_sum)
    return n - (not_sqare_in_pattern * maxprime)

print(solution(8,12))