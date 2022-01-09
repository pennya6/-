#플로이드 워셜 알고리즘
#모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야하는 경우에 사용하는 알고리즘
#각 단계마다 거쳐가는 노드를 기준으로 알고리즘 수행
#2차원 테이블에 최단거리 정보를 저장하는 특징
#다이나믹 프로그래밍 유형 속함 -> 점화식사용

#즉 A->B 최소비용과 A->K->B 최소비용 비교하여 더 작은값 갱신
#특정 노드 k를 거쳐가는 경우 확인

INF=int(1e9)
n=int(input())
m=int(input())

#그래프 초기화 행과 열 
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기자신에서 자기자신 0 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#간선정보
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    
#점화식 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#수행결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INF",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()