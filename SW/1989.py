T = int(input())

for i in range(T) :
    cnt = 1
    test = []
    test.extend(input()) 
    
    for j in range(len(test)//2) :
        if test[j] != test[len(test)-1-j] :
            cnt = 0
            break 
    print("#{}".format(i+1),cnt)

