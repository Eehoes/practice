test = int(input()) # 테스트케이스 개수 입력 받음

for i in range(test) :
    N = int(input()) # 테스트 케이스 번호 입력 받음
    data = list(map(int,input().split())) # 점수 입력 받음
    dic = {}
    
    for j in data :
        if j in dic :
            dic[j] += 1
        else :
            dic[j] = 1
    
    print("#{}".format(N), max(dic,key=dic.get))
            
            
