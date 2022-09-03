#백준 기초
import sys

#1
#  user = input()

# result= print(user+"??!")

#2 서기연도

# user = int(input())

# print(user-543)

# 3체스
# a,b,c,d,e,f = input().split()
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# e=int(e)
# f=int(f)
# chess=[1,1,2,2,2,8]

# print(chess[0]-a,chess[1]-b,chess[2]-c,chess[3]-d,chess[4]-e,chess[5]-f)

# a,b,c= map(int,input().split())

# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print (((a%c) * (b%c))%c)

#곱셈?

# user1 = int(input())
# user2= int(input())

# print(user1*((user2%100)%10))
# print(user1*((user2%100)//10))
# print(user1*(user2//100))
# print(user1*user2)

#고양이를 출력

# print("\\    /\\")
# print(" )  ( \')")
# print("(  /  )")
# print(" \\(__)|")


# 숫자정수 입력
# a=int(input())

# if(90<=a<=100):
#     print("A")
# elif(80<=a<=89):
#     print("B")
# elif(70<=a<=79):
#     print("C")  
# elif(60<=a<=69):
#     print("D")  
# else:
#     print("F")      
#

#윤년
#  user = int(input())

# if(user%4==0 and user%100!=0 or user%400==0):
#     print("1")
# else:
#     print("0")

#알람시계
# h,m=map(int,input().split())

# if m-45<0:
#     h=h-1
#     m=m-45+60
#     if h<0:
#         h=h+24
# else:
#     m=m-45


# print(h,m)
#


#오븐

# h,m=map(int,input().split())

# input = int(input())

# if input+m >= 60:
#     h= h+((input+m)//60)
#     m= (input+m)%60
#     if h>=24:
#         h=h-24
# else:
#     m=input+m
    


# print(h,m)
#주사위3개

# a,b,c=map(int,input().split())

# if a==b==c:
#     result=10000+a*1000
# elif a==b:
#     result=1000+a*100
# elif a==c:
#     result=1000+a*100
# elif b==c:
#     result=1000+b*100
# else:
#     if a>b and a>c:
#         result= a*100
#     elif b>c and b>a:
#         result = b*100
#     else:
#         result = c*100

# print(result)    
    
# a= int(input())

# for i in range(1,10):
#     print("{0} * {1} = {2}".format(a,i,a*i))
#     print(f"{a} * {i} = {a*i}")
#33
# loop=int(input())
# for i in range(loop):
#     a,b=map(int,input().split())
#     print(a+b)

# user = int(input())
# sum=0
# for i in range(user):
#     sum= (i+1)+sum

# print(sum)
#물건계산
# receipt = int(input())
# number = int(input())
# sum = 0
# for i in range(number):
#     a,b=map(int,input().split())
#     sum=a*b+sum
# if receipt == sum:
#     print("Yes")
# else:
#     print("No")

#15552
# input = int(sys.stdin.readline())
# for i in range (input):
#     a,b=map(int,sys.stdin.readline().split())
#     print(a+b)
#11021

# input1 = int(input())
# for i in range(input1):
#     a,b=map(int,input().split())
#     print(f"Case #{i+1}: {a} + {b} = {a+b}")

#2438 별찍기

# user = int(input())
# j=user-1
# for i in range(1,user+1):
#     print(' '*j,end="")
#     print("*"*i)
#     j=j-1

#10871 x보다작은수
# num,user = map(int,input().split())
# a=list(map(int,input().split()))

# for i in range(0,num):    
#     if(a[i]<user):
#      print(f"{a[i]}",end=" ")

#10952 A+B -5
# c=[]
# row =0
# while(True):
#     a,b=map(int,input().split())
#     c.append(a+b)
#     row = row+1
#     if(a==0 or b==0):
#         break
# for i in range(row-1):
#     print(c[i])

#1110 더하기 사이클
# user=int(input()) #입력

# num= user #num에 값저장
# cycle =0 #반복
# if (num<10):
#     num=num*10
#     user=user*10

# while(True):
#     a=(num//10)+(num%10) #십의자리 일의자리 더하기
#     b=((num%10)*10)+(a%10) #새로운수

    
#     C=b
#     num= b
#     cycle=cycle+1

#     if(user==C):
#         print(cycle)
#         break











