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
def word_count(input_str): # 입력 값을 받을때 매개 변수 이름에다가 타입을 넣으면 생각할때 편하다
    # 1. 매개변수로 문자열 => input_str
    # 2. 공백을 찾음 => " " 
    # 3. 공백을 계산
    # 4. 공백 +1 반환
    # n = 0
    # for i in input_str:
    #     if i == " ":
    #         n = n + 1
    # return n + 1

    return len(input_str.split()) # 내장함수 사용, string 이기 때문에 사용 가능

# if, for로 풀수 있는 문제를 출제합니다

def which_team_won(team_A, team_B):
    result_A = (team_A[0] * 3) + (team_A[1] * 2) + (team_A[2] * 1)
    result_B = (team_B[0] * 3) + (team_B[1] * 2) + (team_B[2] * 1)
    if result_A < result_B:
        return "B"
    else:
        return "A"
    
def is_advertisement(input_number):
    temp = list(str(input_number))                  # list를 빼도 동작을 함 => string도 index값을 받음 => 헷갈리기때문에 list를 쓰면 편함(추천)
    if (temp[0] == "8" or temp[0] == "9") and \
        (temp[3] == "8" or temp[3] == "9") and \
        (temp[1] == temp[2]):
        return "광고"
    else:
        return "광고아님"
# \ 를 쓰면 다음 줄로 내릴 수 있다

def where_is_the_ball_located(input_str): # Divide and Conquer 문제
    ball_located = 1
    for swap in input_str:
        if swap == "A":
            if ball_located == 1:
                ball_located = 2
            elif ball_located == 2:
                ball_located = 1
        elif swap == "B":
            if ball_located == 2:
                ball_located = 3
            elif ball_located == 3:
                ball_located = 2
        elif swap == "C":
            if ball_located == 3:
                ball_located = 1
            elif ball_located == 1:
                ball_located = 3

    return ball_located
# 복잡한 문제가 나오면 문제를 분할해서 작게 만들어가지고 푼다 => 연결부분은 elif로 연결한다

def where_is_it_empty(input_lst):
    # 1. 리스트에서 원하는 원소를 가져 와야 됨
    # 2. 위치 비교!
    # 3. 몇개인지?
    # 문자열도 index 사용이 가능하다
    yesterday = input_lst[0]  
    today = input_lst[1]
    
    occupied = 0
    # range
    for i in range(len(today)):
        if yesterday[i] == "F" and today[i] =="F":
            occupied += 1

    return occupied

def the_smallest_city(input_lst):  # min-Max 패턴
    input_lst.sort()
    left = (input_lst[1] - input_lst[0]) / 2
    right = (input_lst[2] - input_lst[1]) / 2
    min_size = left + right
    
    for i in range(2, len(input_lst) - 1):
        left = (input_lst[i] - input_lst[i - 1]) / 2
        right = (input_lst[i + 1] - input_lst[i]) / 2
        if min_size > left + right:
            min_size = left + right
    
    return min_size    

def how_much_more_should_we_earn(input_lst):
    # 1. 리스트 해체
    # 2. 사람 숫자 구해야 됨
    # 3. 사람 숫자 * 금액 총 금액 계산
    # 4. 금액 계산 비교(여행 비용)
    trip_cost = input_lst[0]
    num_jobs = input_lst[-1]
    proportions = input_lst[1:-1]

    job_proportions = []
    for i in proportions:
        _temp = int(num_jobs * i)
        job_proportions.append(_temp)

    total = 0
    COSTS = [12,11,10,9]
    for i in range(len(job_proportions)):
        total = total + (COSTS[i] * job_proportions[i])

    if trip_cost < total / 2:
        return "YES"
    else:
        return "NO"
    
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
    if the_smallest_city(the_smallest_city_input) == 2.5:
        print("5. the_smallest_city 테스트 통과")
    if how_much_more_should_we_earn(how_much_more_should_we_earn_input) == "NO":
        print("6. how_much_more_should_we_earn 테스트 통과")
