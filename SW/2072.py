test = int(input())
all_tests = [list(map(int, input().split())) for i in range(test)]

for j in range(test) :
    for e in range(10) :
        if all_tests[j][e] % 2 == 0 :
            all_tests[j][e] = 0
        
    result = sum(all_tests[j])
    print("#{}".format(j+1),result)
    
    
    