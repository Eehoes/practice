# a = int(input()) # 첫 번째 숫자 입력
# b = int(input()) # 두 번째 숫자 입력

# output_3 = (a*((b%100)%10))
# output_4 = (a*((b%100)//10))
# output_5 = (a*(b//100))
# output_6 = (output_3 + (output_4*10) + (output_5 *100))


# print(output_3)
# print(output_4)
# print(output_5)
# print(output_6)

# 다시 풀어보기
a=int(input())
b=input()

for i in range(1,4):
    print(a*int(b[-i]))
print(a*int(b))