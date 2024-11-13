test = int(input())
all_tests = [list(map(int, input().split())) for i in range(test)]

for i in range(test) :
    average = sum(all_tests[i]) /10
    print("#{}".format(i+1),round(average))

    