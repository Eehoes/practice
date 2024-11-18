T = int(input()) # Test Case 개수 입력
days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for i in range(T) :
    # a_dict= {}
    # b_dict = {}
    result = 0
    
    a_mon, a_day, b_mon, b_day = map(int,input().split())
    
    # a_dict[a_mon] = a_day
    # b_dict[b_mon] = b_day
    
    
    if a_mon < b_mon :
        result = days[a_mon] - a_day + b_day + 1
        for j in range(a_mon+1,b_mon) :
            result += days[j] 
    else :
        result = b_day - a_day +1
    print("#{}".format(i+1), result)

