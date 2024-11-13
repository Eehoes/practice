test = int(input()) # 테스트케이스 개수 입력 
all_tests = [input() for i in range(test)]

days =[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(test) :
    year = int(all_tests[i][:4])
    month = int(all_tests[i][4:6])
    day = int(all_tests[i][6:8])
    
    if month >0 and month <13 and day<=days[month-1] :
        print("#{} {:04d}/{:02d}/{:02d}".format(i + 1, year, month, day))
    else:
        print("#{} -1".format(i + 1))
        