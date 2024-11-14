T = int(input())

for i in range(T) :
    result = []
    sum = 0
    
    num = int(input()) # 영어 개수
    
    # 영어 종류와 개수 입력
    for j in range(num) :
        a,b = input().split()
        b = int(b)
        
        # append 는... 저 값이 각각 list에 들어가는게 아니라 한 뭉텅이로 하나의 값이 되는 것.
        # result.append(a*cnt[a]) 가 아님.
        result.extend([a] * b)
        
        sum += b # 키값의 총합
    
    print("#{}".format(i+1))
    
    for e in range(0,sum,10) :
        print("".join(result[e:e+10]))
        