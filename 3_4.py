# 그리디 - 1이 될때까지
n,k=map(int,input().split())
result=0
while n>=k:
    if n==1:
        break
    elif n%k==0:
        n=n/k
        result+=1
    else:
        n=-1
        result+=1
print(result)
