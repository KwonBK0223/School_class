# 아래 INPUT은 수정하지 마세요.
word_count_input = "No one is an island."
which_team_won_input1 = [3, 2, 1]
which_team_won_input2 = [1, 2, 3]
is_advertisement_input = 8119
where_is_the_ball_located_input = "ABAAACCAABBB"
where_is_it_empty_input = ["FF.", ".F."]
the_smallest_city_input = [20, 50, 4, 19, 15, 1]
how_much_more_should_we_earn_input = [504, 0.2, 0.08, 0.4, 0.32, 125]

# 아래 함수들을 완성하세요. 매개변수는 자유롭게 설정할 수 있습니다.
def word_count(str):
    strings = str.split()
    ans = len(strings)
    return ans

def which_team_won(A,B):
    total_A = (A[0] * 3) + (A[1] * 2) + (A[2] * 1)
    total_B = (B[0] * 3) + (B[1] * 2) + (B[2] * 1)
    ans = ""
    if total_A > total_B:
        ans = "A"
    elif total_B > total_A:
        ans = "B"
    else:
        ans = "Draw"
    return ans

def is_advertisement(num):
    num1 = num//1000
    num2 = (num-(num1*1000))//100
    num3 = (num-(num1*1000)-(num2*100))//10
    num4 = num % 10
    if (num1 ==8 or num1==9) and (num4 ==8 or num4 ==9) and (num2 == num3):
        ans = "광고"
    else:
        ans = "광고아님"
    return ans

def where_is_the_ball_located(str):
    ball = [1,0,0]
    x = len(str)
    for i in range(x):
        if str[i] == "A":
            temp = ball[0]
            ball[0] = ball[1]
            ball[1] = temp
        elif str[i] == "B":
            temp = ball[1]
            ball[1] = ball[2]
            ball[2] = temp
        elif str[i] == "C":
            temp = ball[2]
            ball[2] = ball[0]
            ball[0] = temp
    ans = ball.index(1) + 1
    return ans

def where_is_it_empty(Room):
    yeterday = Room[0]
    today = Room[1]
    ans = 0
    for i in range(len(today)):
        if yeterday[i] == today[i] == "F":
            ans+=1
    return ans

def the_smallest_city():
    pass

def how_much_more_should_we_earn(Brunch):
    cost = Brunch[0]
    A ,B, C, D = Brunch[1],Brunch[2],Brunch[3],Brunch[4]
    num = Brunch[5]
    cost_A = A * num * 12
    cost_B = B * num * 11
    cost_C = C * num * 10
    cost_D = D * num * 9
    cost_sum = (cost_A+cost_B+cost_C+cost_D)/2
    ans=""
    if cost_sum >= cost:
        ans = "NO"
    else:
        ans = "Yes"
    return ans

if __name__=="__main__":
    # 함수 테스트를 위한 코드입니다. 주석을 해제하고 실행하세요.
    if word_count(word_count_input) == 5:
        print("0. word_count 테스트 통과")
    if is_advertisement(is_advertisement_input) == "광고":
        print("1. is_advertisement 테스트 통과")
    if which_team_won(which_team_won_input1, which_team_won_input2) == "A":
        print("2. which_team_won 테스트 통과")
    if where_is_the_ball_located(where_is_the_ball_located_input) == 2:
        print("3. where_is_the_ball_located 테스트 통과")
    if where_is_it_empty(where_is_it_empty_input) == 1:
        print("4. where_is_it_empty 테스트 통과")
    # if the_smallest_city(the_smallest_city_input) == 2.5:
    #     print("5. the_smallest_city 테스트 통과")
    if how_much_more_should_we_earn(how_much_more_should_we_earn_input) == "NO":
        print("6. how_much_more_should_we_earn 테스트 통과")