# <week1>

# age = input("나이를 입력하세요")
# if int(age) < 19:
#     print("할인 되었습니다")
# else:
#     print("할인이 안됩니다")

# print("hello Python")

# print(100)
# print(2+4)
# print(10 +20)
# print(10 - 20)
# print(10 * 20)
# print(10 / 20)
# print(123 * 8765)
# print(10 + 20 * 30)

# x = 100
# y = 200
# print(x+y)

# x = 100
# y = 200
# print("100과 200의 평균 값 :", (x+y)/2)

# <week2>

# width = 10
# height = 5
# width = 20
# rectangle_area = width * height
# print("사각 형의 면적 :", rectangle_area)

# num = 85
# print(type(num))
# pi = 3.14159
# print(type(pi))
# message = "Good morning"
# print(type(message))

# l = [100, 300, 500, 900]
# print(type(l))
# d = {"apple" : 3000, "banana" : 4200}
# print(type(d))
# t = (153, 257)
# print(type(t))

# txt1 = "강이지 이름은 '햇님'이야"
# txt2 = "강아지 이름은 '햇님'이야"
# print(txt1)
# print(txt2)
# txt5 = "banana\napple\norange"
# print(txt5)

# print(0.1 + 0.1 == 0.2)
# print(0.1 + 0.1 + 0.1 == 0.3)
# print(0.1 + 0.1 + 0.1)
# print(0.1 * 19.0)

# print(14/5)
# print(14//5)

# num1 = num2 = num3 = 200
# print(num1, num2, num3)
# num4, num5 = 300, 400
# print(num4, num5)

# x = int(input("정사각형의 밑변을 입력하시오 :"))
# print("정사각형의 면적 :", x**2)

# x = int(input("정수를 입력하세요 :"))
# if x % 2 == 0:
#     print("True")
# else:
#     print("False")

# age = int(input("나이를 입력하세요 :"))
# if age < 20:
#     print("청소년 할인")

# step = int(input("걸음수를 입력하세요 : "))
# if step >= 1000:
#     print("목표달성")

# clock = int(input("현재 시각을 입력하세요 : "))
# if clock < 12:
#     print("오전입니다")
# else:
#     print("오후입니다")

# number = int(input("정수를 입력하세요"))
# if (number % 3 == 0) or (number % 5 == 0):
#     print("3의 배수 또는 5의 배수입니다")

# num = int(input("정수를 입력하세요 "))
# if num > 0:
#     print("양수")
# elif num < 0:
#     print("음수")

# def leap_year(input_year):
#     x = int(input_year)
#     if (x % 4 == 0):
#         if (x % 100 != 0) or (x % 400 == 0):
#             return True
#         elif (x % 100 == 0):
#             return False
#     else:
#         return False
    
# print(leap_year(int(input())))

# def your_grade(input_grade):
#     a = int(input_grade)
#     if a >= 90:
#         return "A"
#     elif a >= 80:
#         return "B" 
#     elif a >= 70:
#         return "C"
#     elif a >= 60:
#         return "D"
#     else:
#         return "F"
    
# score = int(input("점수를 입력하세요. "))
# print(your_grade(score))

# for i in range(5):
#     print(i+1, "Python!")

# for i in range(5):
#     print(i)

# for i in range(5):
#     print(i, end = ' ')

# for i in range(2,5):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# s = 0
# for i in range(1,11):
#     s += i

# print(s)

# a = int(input("정수를 입력하세요. "))
# ans = 0
# for i in range(1,a+1):
#     ans += i
# print(f'1부터 {a}까지의 합은 {ans}입니다')

# def factorial(int_input):
#     ans = 1
#     for i in range(1,int_input + 1):
#         ans *= i
#     return ans

# num = int(input("정수를 입력하세요. "))
# print(factorial(num))

# nums = [11, 22, 33, 44, 55, 66]

# for i in nums:
#     print(i)

# nums = [10, 20, 30, 40, 50]
# ans = 0
# for i in nums:
#     ans += i
# print(ans)

# st = "Hello"
# print(list(st))

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} X {j} = {i * j}',end=' ')
#     print()

# def wndcjq(int_input):
#     for i in range(int_input + 1):
#         print(" "*i + "#")

# wndcjq(int(input()))

# def wndcjq2(int_input):
#     for i in range(int_input):
#         print(" "*(int_input - i) + "#")

# wndcjq2(int(input()))

# def plus_top(num):
#     for i in range(num):
#         print(' ' * (num-i-1) + "+" * ((2 * i) + 1))

# plus_top(5)

# num = int(input())
# for i in range(num,-1,-1):
#     print(i, end = ' ')

# def odd(int_input):
#     for i in range(int_input):
#         print((2 * i) + 1, end = " ")

# odd(int(input()))

# def is_prime(int_input):
#     ans = True
#     if int_input == 2:
#         ans = True
#     else:
#         for i in range(2, int_input):
#             if int_input % i == 0:
#                 ans = False
#     return ans
# print(is_prime(int(input())))
# for i in range(1,100):
#     print(i, end = " ")
#     print(is_prime(i))


# def is_prime(int_input):
#     ans = True
#     if int_input == 2:
#         ans = True
#     else:
#         for i in range(2, int_input):
#             if int_input % i == 0:
#                 ans = False
#     return ans

# ans = []
# for i in range(2,101):
#     if is_prime(i) == True:
#         ans.append(i)
# print(ans)

# <week4>

# def print_star(int_input):
#     for i in range(int_input):

#         print(i+1, "********************")

# print_star(int(input()))

# def print_sum(a,b):
#     print(a + b)
# a, b = map(int,input().split(','))
# print_sum(a,b)

# def print_root(a,b,c):
#     r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#     r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#     print("r1 = ",r1)
#     print("r2 = ",r2)

# print_root(1,2,-8)

# def get_sum(a,b):
#     return a+b

# a, b = map(int,input().split())
# print(get_sum(a,b))

# def fibo(int_input):
#     x0 = 0
#     x1 = 1
#     if int_input == 0:
#         return x0
#     elif int_input == 1:
#         return x1
#     else:
#         for i in range(int_input - 1):
#             temp = x0
#             x0 = x1
#             x1 = temp + x1
#         return x1
    
# for i in range(10):
#     print('피보나치 수열',i, '번째', fibo(i))

# <week5>

# lst = [1 , 2.5, "apple"]
# for i in lst:
#     print(type(i))

# lst = list(range(1,11))
# print(lst)
# print(lst[2])
# print(lst[-1])
# print(lst[-2])
# print(lst[-3])
# print(lst[1:3])
# print(lst[3:])
# print(lst[-3:-1])
# lst.append(123)
# print(lst)
# del lst[3]
# print(lst)
# lst.remove(8)
# print(lst)
# print(lst.index(3))

# <과제1>

# def report4(hour_input, length_input):
#     return length_input / hour_input

# hour, length = map(int,input().split())
# print(report4(hour, length))

# def report5(length_input, velocity_input):
#     return length_input / velocity_input

# length, velocity = map(int,input().split())
# print(report5(length, velocity),"초")
# print(report5(length, velocity) / 60,"분")

# def report6(width_input, height_input):
#     return width_input * height_input

# width, height = map(int,input().split())
# print(report6(width, height))

# def report7(width_input, height_input):
#     return (width_input * height_input) / 2

# width, height = map(int,input().split())
# print(report7(width, height))

# def report8(radius_input):
#     PI = 3.141592
#     return (radius_input ** 2) * PI

# radius = int(input())
# print(report8(radius))

# def report9(int_input):
#     x = str(int_input)
#     x1 = x[0]
#     x2 = x[1]
#     x3 = x[2]
#     return [x1, x2, x3]

# num = int(input())
# ans = report9(num)
# k = ["백의 자리 :","십의 자리 :","일의 자리 :"]
# for i in range(3):
#     print(k[i],ans[i])

# def report10(int_input):
#     x = str(int_input)
#     x1 = x[0]
#     x2 = x[1]
#     x3 = x[2]
#     return [x1, x2, x3]

# num = int(input())
# ans = report9(num)
# k = ["백의 자리 :","십의 자리 :","일의 자리 :"]
# for i in range(2,-1,-1):
#     print(k[i],ans[i])

# <report2>

# def report1(int1, int2):
#     x = [int1, int2]
#     x.sort()
#     for i in range(x[0],x[1]+1):
#         print(i)

# x,y = map(int,input().split())
# report1(x,y)

# def report2(x_input, y_input):
#     if x_input > 0:
#         if y_input > 0:
#             return "1사분면"
#         elif y_input < 0:
#             return "4사분면"
#         else:
#             return "x축위"
#     elif x_input < 0:
#         if y_input > 0:
#             return "2사분면"
#         elif y_input < 0:
#             return "3사분면"
#         else:
#             return "x축위"
#     else:
#         if y_input == 0:
#             return "원점"
#         else:
#             return "y축위"

# x,y = map(int,input().split())
# print(report2(x,y))

# def report3(int_input):
#     if int_input in [1,2,3,4,5,6,7,8,9]:
#         for i in range(1,10):
#             print(f'{int_input} X {i} = {int_input * i}')
#     else:
#         print("1에서 9까지의 수를 다시 입력하세요")

# a = int(input())
# report3(a)

# def report4(int_input):
#     ans = True
#     if int_input == 1:
#         ans = False
#     elif int_input == 2:
#         ans = True
#     else:
#         for i in range(2,int_input):
#             if int_input % i == 0:
#                 ans = False
#     return ans

# for i in range(1,20):
#     if report4(i):
#         print(i,"소수임")
#     else:
#         print(i,"소수아님")

# def report4(int_input):
#     ans = 0
#     for i in range(1, int_input + 1):
#         ans += 1 / (i**2)
#     return ans

# a = int(input())
# print(report4(a))

# <lab1>

# def lab1(str_input):
#     x = str_input.split()
#     return len(x)

# str = input()
# print(lab1(str))

# def lab2(team_A, team_B):
#     score_A = (team_A[0] * 3) + (team_A[1] * 2) + (team_A[2] * 1)
#     score_B = (team_B[0] * 3) + (team_B[1] * 2) + (team_B[2] * 1)
#     if score_A > score_B:
#         return "A"
#     elif score_A < score_B:
#         return "B"
#     else:
#         return "Draw"
    
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# print(lab2(A,B))

# def lab3(num_input):
#     x = str(num_input)
#     if (x[0] == "8" or x[0] == "9") and (x[-1] == "8" or x[-1] == "9") and (x[1] == x[2]):
#         return "광고"
#     else:
#         return "광고아님"

# num = int(input())
# print(lab3(num))

# def lab4(str_input):
#     ans = [1,0,0]
#     for i in str_input:
#         if i == "A":
#             temp = ans[0]
#             ans[0] = ans[1]
#             ans[1] = temp
#         elif i == "B":
#             temp = ans[1]
#             ans[1] = ans[2]
#             ans[2] = temp
#         elif i == "C":
#             temp = ans[2]
#             ans[2] = ans[0]
#             ans[0] = temp
#     return ans.index(1) + 1

# cup = input()
# print(lab4(cup))

# def lab4(day_input,yesterday_input, today_input):
#     ans = 0
#     for i in range(day_input):
#         if yesterday_input[i] == today_input[i] == "F":
#             ans += 1
#     return ans

# day = int(input())
# yesterday = input()
# today = input()
# print(lab4(day, yesterday, today))

# def lab5(lst_input):
#     lst_input.sort()
#     left = (lst_input[1] - lst_input[0]) / 2
#     right = (lst_input[2] - lst_input[1]) /2
#     min_size = left + right

#     for i in range(2, len(lst_input) - 1):
#         left = (lst_input[i] - lst_input[i - 1]) / 2
#         right = (lst_input[i + 1] - lst_input[i]) / 2
#         if min_size > left + right:
#             min_size = left + right
    
#     return min_size

# def lab6(lst_input):
#     MT_cost = lst_input[0]
#     ratio = lst_input[1:-1]
#     num = lst_input[-1]
#     COSTS = [12,11,10,9]
#     brunch = 0
#     for i in range(4):
#         brunch += (ratio[i] * num * COSTS[i])
#     if (brunch / 2) >= MT_cost:
#         return "YES"
#     else:
#         return "NO"

# lst = [504, 0.2, 0.08, 0.4, 0.32, 125]
# print(lab6(lst))

