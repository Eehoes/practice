# test = int(input())

# all_tests = [list(map(int, input().split())) for i in range(test)]

# for i in range(test) :
#     if all_tests[i][0] > all_tests[i][1] :
#         result = '>'
#     elif all_tests[i][0] < all_tests[i][1] :
#         result = '<'
#     else :
#         result = '='
#     print("#{}".format(i+1),result)
    
    
T = int(input()) # Test case 개수
for i in range(T) :
    A,B = map(int,input().split()) # A,B 를 입력 받음
    if A < B :
        result = '<'
    elif A> B:
        result = '>'
    else :
        result = '='
        
    print("#{}".format(i+1),result)
        

  