T = int(input())
all_datas = [] # list로 일단 만듦


for i in range(T) :
    N = int(input()) # 돌 던진 사람의 수
    data = list(map(int,input().split())) # 던진 거리 
    dic = {}
  
for i in range(T) :
    for j in data :
        key_ = abs(j) # 양수로 바꿈
            
        if key_ in dic :
            dic[key_] += 1
        else :
            dic[key_] = 1
    # min_key = min(dic,key=dic.get) # 이거는 빈도수가 가장 작은 값
   
    print("#{}".format(i+1),min(dic.keys()),dic[min(dic.keys())] )

# 근데 이문제 그냥 list에서 abs()를 이용해서 양수로 만든 후 sort 
# 써서 가장 작은 값을 구하면 되는거 아니야? 개수랑.. 
# 이 방법으로도 해보기
    
# -----------------------------------------------  
    # for i in range(test) :
    # N = int(input()) # 테스트 케이스 번호 입력 받음
    # data = list(map(int,input().split())) # 점수 입력 받음
    # dic = {}
    
    # for j in data :
    #     if j in dic :
    #         dic[j] += 1
    #     else :
    #         dic[j] = 1
    
    # print("#{}".format(N), max(dic,key=dic.get))
    
    
        # 보류
    # all_datas.append(data) # 던진거리 list에 넣음
    
    # for j in all_datas :
    #     if j < 0 : # 음수이면
    #         j = -j # -를 붙임
            
    #     min = 100000 
        
    #     if j <= min :
    #         min = j # 거리가 가까운 것을 찾음. 
        