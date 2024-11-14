N = int(input())
list_369 = [] 

for i in range(1,N+1) :
    list_369.append(i) 

list_369 =list(map(str,list_369)) # 숫자를 문자열로 변환

for i in list_369 :
    if '3' in i or '6' in i or '9' in i :
        print('-'*(i.count('3')+i.count('6')+i.count('9')), end = " ")

    else :
        print(i, end=" ")


