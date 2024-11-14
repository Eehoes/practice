T = int(input()) # test case 개수 주어짐
num = [] # 빈 list 선언

for i in range(T) :
    data = int(input())
    num.append(data) # num 아라는 list에 입력받은 data를 넣어줌.

    # cnt = 0 # 개수
   
for i in range(T) :
    dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0} 
    
    print("#{}".format(i+1), end=" ")
    # dictionary 키 dict 
    for j in dict :  # {2,3,5,7,11} 
        
        # if data % j == 0 :
        #     dict[j] +=1
        #     data = data // j    
        
        # data % j 가 0일 때만 실행
        # 즉, data % j != 0 이 되면 빠져나옴
        while num[i]%j == 0 :
            dict[j] += 1 # j라는 키의 '값' 을 +1 해줌
            num[i] = num[i] // j # 그리고 나눠준다.
    
        print(dict[j], end=" ")
    
    print()
            
            
            
            
        
        
    

