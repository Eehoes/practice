test = int(input())

all_tests = [list(map(int, input().split())) for i in range(test)]

for i in range(test) :
    result = max(all_tests[i])
    print("#{}".format(i+1),result)