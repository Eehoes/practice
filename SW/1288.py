T = int(input()) # TestCase 개수
num = {0,1,2,3,4,5,6,7,8,9} # 모든 숫자들이 포함된 '집합'
data = []

for i in range(T) :
    # 아래의 방법은 이미 내가 위에서 data[] 라는 list를 만들었는데
    # list가 빈 리스트라서 안 됨. 아래 방법은 리스트가 요소를
    # 가지고 있을 때만 ㅇㅇ
    # data[i] = int(input()) # 데이터를 입력 받음
    
    data.append(int(input()))

for i in range(T) :
    data_set = set() # 각 테스트케이스마다 추적할 집합 초기화
    cnt = 0 # 몇 번 곱하는지 알기 위한 숫자
    
    # data_set과 num 집합이 같지 않을 때까지 반복
    # 즉, 모든 숫자를 볼 때까지 
    while data_set != num : 
        cnt +=1 # 몇 번 곱하는지 
        current_num = cnt * data[i] 
        
        # 현재 숫자의 각 자릿수를 집합에 추가 
        data_set.update(map(int,str(current_num)))
    
    print("#{}".format(i+1),cnt*data[i])

