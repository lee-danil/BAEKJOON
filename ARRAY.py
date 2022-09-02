# #10818 최솟값 최댓값
# user=int(input())
# n=list(map(int,input().split()))

# print(min(n))
# print(max(n))

#2562번 최댓값
# list=[]
# for i in range(9):
#     list.append(int(input()))

# print(max(list))
# print(list.index(max(list))+1)

#3052 나머지
# list=[]
# list_mod=[]
# for i in range(10): #입력
#     list.append(int(input()))
#     if list[i]%42 not in list_mod:
#         list_mod.append(list[i]%42)


# print(len(list_mod))


#1546 평균
# score =[]
# new_score=[]
# sum=0
# num = int(input())
# score = list(map(int,input().split()))
# max = max(score)
# for i in range(len(score)):
#     new_score.append((score[i]/max)*100)
#     sum=float(sum)+new_score[i]
# print(sum/num)

#8958 Ox퀴즈
# list=[]

# user= int(input()) #입력
# for i in range(user):
#     list=(input())
#     count=1
#     sum=0
#     for i in range(len(list)):
#         if list[i]=='O':
#             sum=sum+1
#             if i>0 and list[i]==list[i-1]=='O':
#                sum=sum+count
#                count+=1
#         else:
#              count=1
#     print(sum)

#4344 평균은 넘겠지

# num = int(input()) #개수

# for i in range(num):
#     score=list(map(int,input().split())) # 학생수 학생별 점수
#     sum =0
#     count=0
#     for j in range(1,len(score)):
#         sum=score[j]+sum

#     avg=sum/score[0]

#     for k in range(1,len(score)):
#         if score[k]>avg:
#          count=count+1
#         else:
#             pass
#     result =count/score[0]
#     print("%.3f"%(result*100)+"%")





