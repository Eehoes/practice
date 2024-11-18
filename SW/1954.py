T = int(input())


for k in range(T) :
    N,M = map(int,input().split()) # A와 B의 문자열 '개수' 를 입력받음
    A = list(map(int,input().split())) # A의 문자열을 입력받음
    B = list(map(int,input().split())) # B의 문자열을 입력받음
    
    # 결과 최대값. 음수도 고려
    result_max = float('-inf')
    
    if N > M : # N(A의 문자열 개수)이 더 크다면?
        for i in range(N-M+1) :
            current_sum = 0
            for j in range (M) :
                current_sum = current_sum  + (A[i+j] * B[j]) 
            result_max = max(result_max, current_sum)
                
    else :
        for i in range(M-N+1) :
            current_sum = 0
            for j in range(N) :
                current_sum  = current_sum  +(A[j] * B[i+j])
            result_max = max(result_max, current_sum)
                
    print("#{}".format(k+1),result_max)

