# 10809번 알파벳 찾기


# user =input() #입력
# alpha="abcdefghijklmnopqrstuvwxyz"
# for i in alpha:
#     if i in user:
#         print(user.index(i),end=' ')
#     else:
#         print("-1",end=' ')

#2675 문자열반복

# user=int(input()) #입력개수
# for i in range(user):
#     num,case=input().split()
#     num=int(num)
#     for j in case:
#         print(num*j,end='')
#     print()

#1157 단어 공부★★
# user = input().upper()

# user_set= set(user)
# user_set= sorted(user_set)
# count=0
# result=[]
# for i in user_set:
#     count = user.count(i)
#     result.append(count)
# if result.count(max(result)) >=2:
#     print("?")
# else: 
#     number=result.index(max(result))
#     print(user_set[number])

#1152 단어의개수

# user = list(map(str,input().split()))

# print(len(user))

#2908 상수

# a,b=list(map(str,input().split()))
# a_list=[]
# b_list=[]
# for i in a[::-1]:
#     a_list.append(i)
# for j in b[::-1]:
#     b_list.append(j)

# a_list=str.join("",a_list)
# b_list=str.join("",b_list)
# if int(a_list) > int(b_list):
#     print(a_list)
# else:
#     print(b_list)

#5622 다이얼

# alpha=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
# user =input()
# sum=0
# for i in user:
#     number=ord(i)-65
#     sum+=alpha[number]+1
# print(sum)

#2941 크로아티아 알파벳

# user = input()

# alpha=["c=",'c-','dz=','d-','lj','nj','s=','z=']

# for i in alpha:
    
#     user = user.replace(i, "*")

# print(len(user))



#1316 그룹단어체커 ★★★★ result -1 , 인덱스슬라이싱

# num =int(input()) 
# result=num

# for i in range(num):
#     user=input() 
#     for j in range(len(user)-1):
#         if user[j] == user[j+1]:
#             pass
#         elif user[j] in user[j+1:]:
#             result -=1
#             break
# print(result)
