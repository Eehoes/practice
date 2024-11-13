str = input() # 문자열입력받음
result=[0] *200

for i in range(len(str)) :
    # ord('A') : 아스키코드 A : 65
    result[i] = ord(str[i])-64
    print(result[i],end =" ")
