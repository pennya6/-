#미래도시
INF=int(1e9)
n,m=map(int,input().split()) #회사개수, 경로개수
graph=[[INF]*(n+1) for _ in range(n+1)] #그래프 초기화

#자기자신으로 가능 경우 0처리
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#간선정보 입력
for _ in range(m):
    a,b=map(int,input().split())
    #서로에게 가는 거리 비용 1
    graph[a][b]=1
    graph[b][a]=1

#점화식
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

x,k=map(int,input().split())
distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print('-1')
else:
    print(distance)


