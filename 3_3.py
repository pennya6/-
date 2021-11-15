#그리디 - 숫자카드게임

#min()함수 사용경우
# n,m=map(int,input().split())
#
# result=0
# for i in range(n):
#     data=list(map(int,input().split()))
#     min_value=min(data)
#     result=max(result,min_value)
#
# print(result)

#반복문 구조
n,m=map(int,input().split())
result=0
for i in range(n):
    data=list(map(int,input().split()))
    minv=10001
    for a in data:
        minv=min(minv,a)
    result=max(result,minv)

print(result)
