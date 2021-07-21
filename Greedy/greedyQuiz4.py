#만들 수 없는 금액
N = int(input())
coins = list(map(int, input().split()))
for i in range(1,9999):
    new_coins = coins.copy()
    if(i in new_coins): #화폐 단위이면 패스
        continue
    else: #화폐 단위가 아니면 검사(있는 화폐로 만들 수 있는지 없는지)
        change = i-1
        j = i
        while(j!=0):
            if(len(new_coins)==0 or min(new_coins)>j): #이제 만들 수 있는 게 없으면
                break
            if(change in new_coins):
                new_coins.remove(change)  # 그 동전 썼으면 제외
                j= j - change
                change = j
            else:
                change = change-1
        if(j!=0):
            break
        else:
            continue #i가 0이 되면 continue
print(i)



