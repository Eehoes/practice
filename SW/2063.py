# 문제 조건 중 숫자의 개수는 무조건 홀수 -> array 후에 인덱스의 중간값을 찾으면 되지 않을까?

test = int(input())

num = list(map(int, input().split())) # 숫자 입력. 
num.sort() # 정렬

print(num[(test-1)//2])

