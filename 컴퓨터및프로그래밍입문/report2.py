# 1번
# a = int(input("첫번째 숫자를 입력하세요 : "))
# b = int(input("두번째 숫자를 입력하세요 : "))
# if a >= b:
#     for i in range(b,a+1):
#         print(i)
# else:
#     for i in range(a,b+1):
#         print(i)

# 2번
# x = int(input("x좌표를 입력하세요 : "))
# y = int(input("y좌표를 입력하세요 : "))
# if x > 0:
#     if y > 0:
#         print("1사분면")
#     elif y < 0:
#         print("4사분면")
#     else:
#         print("x축 또는 y축에 위치합니다")
# elif x < 0:
#     if y > 0:
#         print("2사분면")
#     elif y < 0:
#         print("3사분면")
#     else:
#         print("x축 또는 y축에 위치합니다")
# else:
#     print("x축 또는 y축에 위치합니다")

# 3번
# n = int(input("1~9 사이의 정수를 입력하세요."))
# if n in [1,2,3,4,5,6,7,8,9]:
#     for i in range(1,10):
#         print(n,'X',i,'=',n*i)
# else:
#     print("1에서 9까지의 수를 다시 입력하세요.")

# 4번
# n = int(input("양의 정수를 입력하세요"))
# ans = "소수입니다"
# if n <= 1 :
#     ans = "소수가 아닙니다"
# for i in range(2,n):
#     if n%i ==0:
#         ans="소수가 아닙니다"
# print(ans)

# 5번
# n = int(input("양의 정수를 입력하세요."))
# ans = 0
# for i in range(1,n+1):
#     ans += 1/(i**2)
# print(ans)