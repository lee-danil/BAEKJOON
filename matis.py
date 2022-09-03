# import math
# # # # #1712 손익분기점

# # # # a,b,c=map(int,input().split()) # 고정비용 # 노트북생산비용 # 노트북가격


# # # # if b>=c:
# # # #     print("-1")
# # # # else:
# # # #     print(a//(c-b)+1)


# # # #벌집 2292
# # # user= int(input())
# # # index=1
# # # sum=1
# # # count=1
# # # while True:
# # #     if user > sum:
# # #         index+=1
# # #         sum+=6*count
# # #         count+=1
# # #     else:
# # #         print(index)
# # #         break

# # #1193 분수찾기 

# # # user = int(input())
# # # row=1
# # # while True:
# # #     if user <= row*(row+1)//2:
# # #         break
# # #     else:
# # #         row+=1
# # # position = user - (row-1)*(row)//2
# # # if row%2==1:
# # #     print(row-position+1,"/",position,sep="")
# # # else:
# # #     print(position,"/",row-position+1,sep="")

# # #2869 달팽이는 올라가고 싶다 ★★★★

# # # A,B,V=map(int,input().split())
# # # q,r=divmod(V-A, A-B)
# # # print(q+1 if not r else q+2)
    
# # #10250 ACM 호텔

# # # num = int(input())
# # # for i in range(num):
# # #     H,W,N=map(int,input().split())
# # #     q,r= divmod(N, H)
# # #     if r==0:
# # #         print(H*100+q)
# # #     else:
# # #         print(r*100+q+1)

# # #2775. 부녀회장이 될테야 ★★★★

# # # user = int(input())

# # # apart=[[0]*15 for _ in range(15)]
# # # apart[0]= [x for x in range(15)]

# # # for i in range(1,15):
# # #     for j in range(1,15):
# # #         for k in range(1,j+1):
# # #             apart[i][j]=apart[i-1][j]+apart[i][j-1]

# # # for i in range(user):
# # #     a=int(input())
# # #     b=int(input())
# # #     print(apart[a][b])

# # #2839 설탕배달

# # # user = int(input())
# # # count=0
# # # while user>=0:
# # #     if user%5==0:
# # #        count+=user//5
# # #        print(count)
# # #        break
# # #     user-=3
# # #     count+=1
# # # else:
# # #     print("-1")
    

# # #10757 큰수 A+B

# # a,b=map(int,input().split())
# # print(a+b)

# # #1978 소수 찾기

# # user = int(input())
# # a_list=list(map(int,input().split()))
# # check=0
# # for i in a_list:
# #     cnt=0
# #     if i==1:
# #         continue
# #     for j in range(2,i+1):
# #         if i%j==0:
# #             cnt+=1
# #     if cnt<=1:
# #         check+=1
# # print(check)
        

# # list=[2,3,4,5,6,7,8,9]
# # for n in list:
# #     is_prime = True
# #     for i in range(2,n):
# #         print(i)
# #         if(n%i==0):
# #             is_prime=False
# #             break

# #     if(is_prime):
# #          print(n,"소수")
# #     else:
# #         print(n,"xxxx")

# #2581 소수

# # m=int(input())
# # n=int(input())
# # result=[]
# # for i in range(m,n+1):
# #     is_prime=True
# #     if i==1:
# #         continue

# #     for j in range(2,i):
# #         if i%j==0:
# #             is_prime=False
# #             break
# #     if (is_prime):
# #         result.append(i)
# # if len(result)!=0:
# #     print(sum(result))
# #     print(min(result))
# # else:
# #    print(-1)

# #11653 소인수분해 ★

# # user = int(input())
# # moc=2
# # count=0
# # while user>1:
# #     if user%moc!=0:
# #         moc+=1
# #     else:
# #         user=user//moc
# #         count+=1
# #         print(moc)   

# # 소인수분해 원리적용 ★★★
# # user = int(input())
# # moc=2
# # sqrt=int(math.sqrt(user))
# # while moc <= sqrt:
# #     if user%moc!=0:
# #         moc+=1
# #     else:
# #         print(moc) 
# #         user = user//moc
# # if user >1:
# #     print(user)   

# #소수 구하기
# # import math
# # m,n=map(int,input().split())

# # result=[]
# # a=0
# # for i in range(m,n+1):
# #     is_prime=True
# #     if i==1:
# #         continue
# #     for j in range(2,int(math.sqrt(i)+1)):
# #         if i%j==0:
# #             is_prime=False
# #             break        
# #     if (is_prime):
# #         result.append(i)
# #         print(result[a])
# #         a+=1


# #골드바흐의추측 ★★★
# import math
# n=10000

# flag= [True]*(n+1)
# flag[0],flag[1]=False,False

# result=[]
# for i in range(2,int(math.sqrt(n)+1)):
#     if (flag[i]):
#         for j in range(i*i,n+1,i):
#             flag[j]=False

# num = int(input())
# for k in range(num):
#     user=int(input())
#     q=r=user // 2
#     while True:
#         if flag[q]==flag[r]==True and flag[q]==flag[r]:
#             print(q,r)
#             break
#         elif flag[q]==flag[r]==True and (q+r)==user:
#             print(q,r)
#             break
#         else:
#             q-=1
#             r+=1





    