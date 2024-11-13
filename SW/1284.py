T = int(input())
all_data = []


for i in range(T) :
    data = list(map(int,input().split())) 
    all_data.append(data) 
    
for i in range(T) :
    A_cost = all_data[i][0]*all_data[i][4] # A사의 요금
    
    if all_data[i][4]<=all_data[i][2] :
        B_cost = all_data[i][2] 
    else :
        B_cost = all_data[i][1] + (all_data[i][4]-all_data[i][2])*all_data[i][3]
    
    print("#{}".format(i+1), min(A_cost,B_cost))

