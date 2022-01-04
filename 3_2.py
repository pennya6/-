#큰수의 법칙
#n:배열의 크기, M:숫자회수, K:연속회수
n,m,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
#print(data[n-1])
first=data[n-1]
second=data[n-2]
#8%3=2...2 -> m%k
# 3*2 +2 ->first*(k*(m%k))+2*second
print(first*(k*(m%k))+2*second)

