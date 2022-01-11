#1로 만들기
#다이나믹 프로그래밍은 문제를 풀기전에 도식화 할 필요가 있음 -> 함수호출과정에서 동일하게 여러번 호출하는 함수들이 존재
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

#보텀업 방식
def bottom_up(x):
    count=0
    dp=[0]*30001
    for i in range(2,x+1):
        dp[i]=dp[i-1]+1
        if i%2==0:
            dp[i]=min(dp[i],dp[i//2]+1)
        if i%3==0:
            dp[i]=min(dp[i],dp[i//3]+1)
        if i%5==0:
            dp[i]=min(dp[i],dp[i//5]+1)
    return dp[x]

print(bottom_up(x))