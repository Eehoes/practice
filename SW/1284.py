T = int(input()) # test case 개수
all_data = [] # test case 저장할 list 


for i in range(T): 
    data = list(map(int, input().split())) # data 입력 
    all_data.append(data)

for i in range(T) :
    P = all_data[i][0] # A사 1L당 요금 P
    Q = all_data[i][1] # B사 기본 요금
    R = all_data[i][2] # 기준 R리터.
    S = all_data[i][3] # B사 추가 사용시 1L 당 요금 S
    W = all_data[i][4] # 사용량 W리터.

    a_cost = P * W
    if W <= R :
        b_cost = Q
    else :
        b_cost = (W-R)*S + Q
    
        
    print("#{}".format(i+1),min(a_cost,b_cost))
    

