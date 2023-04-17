# def leap_year(year_input):
#     x = int(year_input)
#     ans = "윤년"
#     if x % 4 == 0:
#         if x % 100  == 0:
#             ans = "윤년 x"
#             if x % 400 == 0:
#                 ans = "윤년"
#     else:
#         ans = "윤년아님"
#     return ans

# while 1:
#     year = int(input())
#     if year == -1:
#         break
#     print(leap_year(year))

# def fibo(num_input):
#     x = 0
#     y = 1
#     if num_input == 0:
#         return x
#     elif num_input == 1:
#         return y
#     else:
#         for i in range(num_input - 1):
#             temp = x
#             x = y
#             y += temp
#     return y

# for i in range(30):
#     print(i, fibo(i))

# def is_prime(int_input):
#     ans = "소수O"
#     if int_input == 1:
#         ans = "소수X"
#     elif int_input == 2:
#         ans = "소수O"
#     else:
#         for i in range(2,int_input):
#             if int_input % i == 0:
#                 ans = "소수X"
#     return ans

# for i in range(1,30):
#     print(i, is_prime(i))

# def small(input_lst):
#     input_lst.sort()
#     left = (input_lst[1] - input_lst[0]) / 2
#     right = (input_lst[2] - input_lst[1]) / 2
#     min_size = left + right
#     for i in range(2, len(input_lst) - 1):
#         left = (input_lst[i] - input_lst[i-1])/2
#         right = (input_lst[i+1] - input_lst[i])/2
#         if min_size > left + right:
#             min_size = left + right
#     return min_size

# def leap_year(year_input):
#     x = int(year_input)
#     ans = "윤년 O"
#     if x % 4 == 0:
#         if x % 100 == 0:
#             ans = "윤년 X"
#             if x % 400 == 0:
#                 ans = "윤년 O"
#     else:
#         ans = "윤년 X"
#     return ans

# while 1:
#     year = int(input())
#     if year == -1:
#         break
#     print(leap_year(year))

# def is_prime(int_input):
#     ans = "소수 O"
#     if int_input == 1:
#         ans = "소수X"
#     elif int_input == 2:
#         ans = "소수O"
#     else:
#         for i in range(2, int_input):
#             if int_input % i == 0:
#                 ans = "소수 X"
#     return ans

# def fibo(int_input):
#     x = 0
#     y = 1
#     if int_input == 0:
#         return x
#     elif int_input == 1:
#         return y
#     else:
#         for i in range(int_input -1):
#             temp = x
#             x = y
#             y += temp
#         return y
    

# for i in range(30):
#      print(i, fibo(i))

def min_max(lst_input):
    lst_input.sort()
    left = (lst_input[1] - lst_input[0]) / 2
    right = (lst_input[2] - lst_input[1]) / 2
    min_size = left + right
    for i in range(2, len(lst_input) - 1):
        left = (lst_input[i] - lst_input[i - 1]) / 2
        right = (lst_input[i + 1] - lst_input[i]) / 2
        if min_size > left + right:
            min_szie = left + right
    return min_size

def word_count(str_input):
    ans = str_input.split()
    return len(ans)

def whick_team_win(team_A, team_B):
    score_A = (team_A[0] * 3) + (team_A[1] * 2) + (team_A[3] * 1)
    score_B = (team_B[0] * 3) + (team_B[1] * 2) + (team_B[3] * 1)
    if score_A > score_B:
        return "A"
    elif score_B > score_A:
        return "B"
    else:
        return "Draw"
    
def is_advertisement(int_input):
    str = str(int_input)
    if (str[0] == "8" or str[0] == "9") and (str[-1] == "8" or str[-1] == "9") and (str[1] == str[2]):
        return "광고"
    else:
        return "광고아님"

def where_is_the_ball(str_input):
    ans = [1,0,0]
    for i in str_input:
        if i == "A":
            temp = ans[0]
            ans[0] = ans[1]
            ans[1] = temp
        elif i == "B":
            temp = ans[1]
            ans[1] = ans[2]
            ans[2] = temp
        elif i == "C":
            temp = ans[2]
            ans[2] = ans[0]
            ans[0] = temp
    return (ans.index(1)) + 1

def where_is_it_empty(day, yes_input, tod_input):
    ans = 0
    for i in range(day):
        if yes_input[i] == tod_input[i] == "F":
            ans += 1
    return ans
def the_smallest_city(lst_input):
    lst_input.sort()
    left = (lst_input[1] - lst_input[0]) / 2
    right = (lst_input[2] - lst_input[1]) / 2
    min_size = left + right
    for i in range(2, len(lst_input) - 1):
        left = (lst_input[i] - lst_input[i-1]) / 2
        right = (lst_input[1+1] - lst_input[i]) / 2
        if min_size > left + right:
            min_size = left + right
    return min_size

def how_much_more_should_we_earn(lst_input):
    MT_cost = lst_input[0]
    ratio = lst_input[1:5]
    total_num = lst_input[-1]
    num = [0,0,0,0]
    for i in range(4):
        num[i] = ratio[i] * total_num
    COSTS = [12,11,10,9]
    brunch_cost = 0
    for i in range(4):
        brunch_cost += num[i] * COSTS[i]
    if (brunch_cost) / 2 >= MT_cost:
        return "YES"
    else:
        return "NO"
    