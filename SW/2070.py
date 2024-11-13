test = int(input())

all_tests = [list(map(int, input().split())) for i in range(test)]

for i in range(test) :
    if all_tests[i][0] > all_tests[i][1] :
        result = '>'
    elif all_tests[i][0] < all_tests[i][1] :
        result = '<'
    else :
        result = '='
    print("#{}".format(i+1),result)
    