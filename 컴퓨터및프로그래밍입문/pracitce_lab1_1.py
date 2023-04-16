"""
해당 Lab은 플라토에서 중간고사를 시행하기 이전에 진행되는 연습
- 100분안에 4문제(자신이 선택한)를 풀어보시면 됩니다.
- 모든 입력은함수의 인자 및 매개변수를 활용하세요

해당 Lab 진행시 교재 뿐만 아니라 Online 자료를 참고해서 진행하세요
- 중간고사에서는 교재 및 online 사용이 금지됩니다.

해당 Lab 진행시 어려움이 있으면 언제든 질문하세요.

해당 Lab 진행시 코드 작성이 어렵다면, 주석을 활용해서 자신의 생각을 적어보세요.

해당 과제의 해설은 6주차 월요일에 진행합니다.
"""

# <0.단어 수 세기(word_count)>
# 제공된 잔어의 수를 세어보세요. 여기서 말하는 단어는 일련의 소문자들입니다.
# 입력 : 소문자와 공백으로 구성된 한 줄의 문자열
# 출력 : 입력된 라인의 단어 수를 출력

# ans = list(input().split())
# print(len(ans))

# <1.누가 이긴 걸까?(which_team_won)>
# 농구에서 점수를 얻는 방법은 3가지로 "3점"슛, "2점"슛, "1점" 자유투가 있습니다.
# 각팀의 득점 성공횟수를 기록했습니다. 경기 결과는?
# 입력 : 각팀(A,B)의 3점,2점,1점 득점 횟수
# 출력 : 경기결과

# A=list(map(int,input().split(',')))
# B=list(map(int,input().split(',')))

# total_A = (A[0] * 3) + (A[1] * 2) + (A[2] * 1)
# total_B = (B[0] * 3) + (B[1] * 2) + (B[2] * 1) 

# if total_A > total_B:
#     print("A")
# elif total_A < total_B:
#     print("B")
# else:
#     print("Draw")

# <2.누굴까(is_advertisement)>
# 전화번호 4자리를 사용해서 누구인지 확인할 수 있습니다.
# 다음 세가지 조건을 모두 충족하는 4자리는 광고 전화입니다.
# 첫번째 숫자는 8또는 9입니다. 네번째 숫자는 8또는 9입니다.
# 두번째와 세번째수는 동일합니다.
# 입력 : 네 자리 숫자
# 출력 : 광고/광고 아님

# num = input()
# num = list(num)
# for i in range(4):
#     num[i] = int(num[i])
# if (num[0]==8 or num[0]==9) and (num[3]==8 or num[3]==9) and (num[1]==num[2]):
#     print("광고")
# else:
#     print("광고아님")

# <3.공의 위치는(where_is_the_ball_located)?>
# 앞 놓여진 3개가 나란히 놓여있습니다. 컵의 위치는 왼쪽(1), 가운데(2),오른쪽(3)
# 공은 가장 왼쪽(1) 안에 있습니다. 컵의 위치를 무작위로 교환할때 공의 위치를 출력
# 컵의 교환방법 3가지
# A:왼쪽컵과 가운데컵 교환, B:가운데 컵과 오른쪽 컵 교환
# C:왼쪽컵과 오른쪽컵 교환

# ball = [1,0,0]
# change = input()
# for i in change:
#     if i == "A":
#         temp = ball[0]
#         ball[0] = ball[1]
#         ball[1] = temp
#     elif i == "B":
#         temp = ball[1]
#         ball[1] = ball[2]
#         ball[2] = temp
#     elif i == "C":
#         temp = ball[2]
#         ball[2] = ball[0]
#         ball[0] = temp
# ans = ball.index(1)+1
# print(ans)

# <4.어디가 비어 있나요(where_is_it_empty)?>
# n개의 공간을 대여하는 일을 하고 있습니다. 각 공간의 점유 여부를 기록합니다.
# 어제와 오늘 모두 점유된 공간의 수를 표시하세요.
# 입력 : 첫번째줄 - 관리하는 공간의 수(1~100)
#       두번째줄 - 어제 공간정보
#       세번째줄 - 오늘의 공간정보
# 출력 : 어제와 오늘 점유된 공간의 수를 출력

# num = int(input())
# yesterday = input()
# today = input()
# ans = 0
# for i in range(num):
#     if yesterday[i]==today[i]=="F":
#         ans+=1
# print(ans)

# <5.가장 작은 도시는(the_smallest_city)?
# 직선 도로 위에 n개의 도시가 각기 다르게 배치 되어있습니다. 한 도시의 이웃은
# 그 도시의 다음으로 작은 도시이고, 오른쪽 이웃은 그 다음으로 큰 위치에 있는
# 도시입니다.

# <6.얼마를 더 모아야할까(how_much_more_should_we_earn)?>
# MT에 필요한 돈을 모으기 위해 브런치 프로그램을 준비하였습니다.
# 브런치에 참가하려면 A직급은 12, B직급은 11, C직급은 10, D직급은 9의 비용 냄
# 브런치를 통해 모인 돈중 50%는 MT비용 사용가능
# 여행비용, 직급비율, 총참여자수를 알 수 있다. 돈을 더 모아야할까?
# 입력 : 비용(50,50000), 직급별 참여 숫자(4개숫자, 합은1.0), 참여자수(4~2000)
# 출력 : Yes/No

# brunch = list(map(float,input().split(",")))
# cost = brunch[0]
# A_num = brunch[1] * brunch[5]
# B_num = brunch[2] * brunch[5]
# C_num = brunch[3] * brunch[5]
# D_num = brunch[4] * brunch[5]
# now = (A_num*12) + (B_num*11) + (C_num*10) + (D_num*9)
# if (now/2)>=cost:
#     print("Yes")
# else:
#     print("No")

# <7.몇 단어를 사용했나요?>
# 