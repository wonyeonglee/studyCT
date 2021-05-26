#1로 만들기

mods = [5,3,2]
result =0
x = int(input())
while x!=1:
    if(x%5!=0):
        x=x-1
        result =result+1
    else:
        for mod in mods:
            if(x%mod ==0):
                x = x//mod
                result=result+1
print(result)
