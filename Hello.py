# 주사위 2개 던지기~
# n,m=input().split()
# n= int(n)
# m=int(m)
# for i in range(1, n+1) :
#   for j in range(1, m+1) :
#     print(i, j)


# 직사각형 별찍기

# a,b=input().split()
# a=int(a)
# b=int(b)

# for j in range(b):
#     for i in range(a):
#      print("*",end="")
#     print('')

# def comple(m,n):
#     result = 0
#     for i in range(m,n+1):
#         print(i)

#     return result

# a= int(80)
# b= a**(1/2)
# print(b)

# class person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age =age
#     def __str__(self):
#         return "저의이름은 {0} 이며 나이는 {1}입니다.".format(self.name,self.age)
# class korea(person):
#     pass

# name=korea("danil",14)
# print(name)

#그리디 알고리즘 탐욕법
#동전 횟수? 코인 나누기


# def coin(n):
#     count =0
#     a=[500,100,50,10]
#     for i in range(len(a)):
#         count += n//a[i] #몫계산 
#         n = n%a[i] #나머지 계산
#         print(count)
# coin(1260)

# 1이될떄 까지


# def nk(n,k):
#     count=0
#     while (n!=1):    
#         if (n%k==0):
#             n= n//k
#             count += 1        
#         else:
#             n=n-k
#             count += 1

# nk(25,3)
# nk(25,5)

# n=int(30)
# k=int(3)
# result =0
# count = 0
# while n!=1:
#     if(n%k==0):
#         count += 1
#         n = n//k
#     else:
#         n=n-1
#         count += 1
# print(count)
        

# print(25%5)
# print(25//5)


#숫자크기합
# user = input()
# sum = int(user[0])

# for i in range(1,len(user)):
#     num=int(user[i])
#     if sum<=1 or num<=1:
#         sum +=num
#     else:
#         sum*=num
# print(sum)
# print(len(user))
# print(user[i])

# # user = int(input())
# count = list(map(int, input().split()))
# count.sort()

# sum =0 #모험가수
# result =0 #그룹수
# # 2 3 3 4 5
# for i in count:
#     sum +=1
#     if sum >= i:
#         result +=1
#         sum=0

# print(result)
    
# user = input().split()
# user.sort()
# print(user)

#좌표
# x,y=2,2

# dx=[0,-1,0,1]
# dy=[1,0,-1,0]

# for i in range(4):
#     nx = x +dx[i]
#     ny = y +dy[i]
#     print(nx,ny)

# n= int(input())
# x,y=1,1
# moveto = input().split()
# #RRRUDD
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move =['L','R','U','D']

# for j in moveto:
#     for i in range(len(move)):
#         if j==move[i]:
#             nx = x +dx[i]
#             ny = y +dy[i]
#     if nx< 1 or ny < 1 or nx > n or ny >n:
#         continue
#     x,y=nx,ny
#     print(x,y)
# print(x,y)

#문자열 재정렬

# user = input()
# result =[]
# sum= 0
# for i in user:
#     if i.isalpha():
#         result.append(i)
#     else:
#         sum +=int(i)
# result.sort()
# result.append(str(sum))
# print(",".join(result))

# a,b=(input().split())
# a=int(a)
# b=int(b)

# c=print(a+b)
# c=print(a-b)
# c=print(a*b)
# c=print(a//b)
# c=print(a%b)