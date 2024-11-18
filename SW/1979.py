T = int(input())

for i in range(T) :
    N,K = map(int,input().split()) # N: N x N 의 원,, K: N 길이의 단어.
    test = []
    cnt = 0

    for j in range(N) : # N개의 행 입력 받음
        row = input().split # 한 행씩 입력받아 리스트로 변환.
        test.append(row)

    # 입력 끝 -----------------------------------------------------------
    
    for row_index in range(N) :
        row = test[row_index]
        
        for col_index in range(len(row) - K+1) :
            if all(row[col_index + offset] == '1' for offset in range(K)):
                cnt+=1
                
    

    
