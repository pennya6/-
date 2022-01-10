#1로 만들기
x=int(input())
# while x>=1:
#     if x==1:
#         print(count)
#     if x%5==0:
#         x=x/5
#         count+=1
#     elif x%3==0:
#         x/=3
#         count += 1
#     elif x%2==0:
#         x/=2
#         count += 1
#     else:
#         x-=1
#         count += 1

def dynamic(x):
    count=0
    if x==1:
        return count
    if x%5==0:
        print(x)
        count=count+1
        return dynamic(x/5)
    elif x%3==0:
        count += 1
        return dynamic(x/3)
    elif x%2==0:
        count += 1
        return dynamic(x/2)
    else:
        count += 1
        return dynamic(x+1)

#보텀업 방식
def bottom_up(x):
    count=0
    dp=[0]*100
    dp[0]=1
    dp[1]=5

print(dynamic(x))