#전보 -> 다익스트라 사용
import heapq
import sys

input=sys.stdin.readline()

INF=int(1e9) #무한의미

n,m,c=map(int,input().split()) #도시의개수,통로의개수,도시C
graph=[[]for i in range(n+1)] #노드에 대한 정보 담는 리스트
distance=[INF]*(n+1) #최단거리 테이블 초기화

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append(y,z) #x->y 비용 z

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작노드로 가기 위한 최단경로 0설정, 큐 삽입
    distance[start]=0
    while q: #큐가 비어있지 않다면
        dist,now=heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now]<dist:
            continue
        for i in graph[now]: #현재 노드와 연결된 다른 인접한 노드들을 확인
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(cost,i[0])
dijkstra(c)
count=0
max_distance=0
for d in distance:
    for d in distance:
        if d!=INF:
            count+=1
            max_distance=max(max_distance,d)
print(count-1,max_distance)