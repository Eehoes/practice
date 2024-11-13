test = int(input())  # 테스트 케이스 개수 입력
results = []  # 결과를 저장할 리스트

for i in range(test):
    a, b = map(int, input().split())
    result = "#{} {} {}".format(i + 1, a // b, a % b)  # 각 테스트 케이스 결과 문자열 생성
    results.append(result)  # 결과 리스트에 추가

# 모든 결과를 한 번에 출력
print("\n".join(results))
