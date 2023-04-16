# 0. 단어수 세기
# lst = list(input().split())
# ans = len(lst)
# print(ans)

# 1. 누가 이긴걸까?
# A = list(map(int,input().split(',')))
# B = list(map(int,input().split(',')))
# total_A = (A[0]*3) + (A[1]*2) + (A[2]*1)
# total_B = (B[0]*3) + (B[1]*2) + (B[2]*1)
# if total_A > total_B:
#     print("A")
# elif total_B > total_A:
#     print("B")
# else:
#     print("Draw")

# 2. 누굴까?
# num = input()
# if (num[0]=='8' or num[0]=='9') and (num[3]=='8' or num[3]=='9') and (num[1] == num[2]):
#     print("광고")
# else:
#     print("광고아님")

# 3. 공의 위치는?
# ball=[1,0,0]
# cup = input()
# for i in cup:
#     if i == "A":
#         temp = ball[0]
#         ball[0] = ball[1]
#         ball[1] = temp
#     elif i == "B":
#         temp = ball[1]
#         ball[1] = ball[2]
#         ball[2] = temp
#     elif i =="C":
#         temp = ball[2]
#         ball[2] = ball[0]
#         ball[0] = temp
# ans = ball.index(1) + 1
# print(ans)

# 4. 어디가 비어 있나요?
# ans = 0
# num = int(input())
# yesterday = input()
# today = input()
# for i in range(num):
#     if yesterday[i] == today[i] == "F":
#         ans+=1
# print(ans)

# 5. 가장 작은 도시는?

# 6.얼마를 너 모아야 할까
# cost, A, B, C, D, num = map(float,input().split(','))
# cost_A = num * A * 12
# cost_B = num * B * 11
# cost_C = num * C * 10
# cost_D = num * D * 9
# brunch = (cost_A + cost_B + cost_C + cost_D) / 2
# print(brunch)