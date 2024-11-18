T = int(input())

for i in range(T) :
    N = int(input())
    input_list = list(map(int,input().split())) # 숫자 입력받아 list에 넣음

    input_list.sort() # 오름차순 정렬
    print("#{}".format(i+1), end = " ")
    for j in range(N) :
        print(input_list[j], end=" ")
    