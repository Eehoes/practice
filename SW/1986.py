T = int(input()) # Test Case 개수

for i in range(T) :
    num_sum = 0 
    
    num = int(input()) 
    for j in range(1,num+1) :
        if j % 2 == 0 :
            num_sum += -j 
        else :
            num_sum += j
    
    print("#{}".format(i+1), num_sum)

