#개선된 다익스트라 알고리즘
#V:노드 개수, E:간선개수
#힙자료구조 사용 -> 특정노드까지의 최단거리에 대한 정보를 힙에 담아서 처리
#힙 -> 우선순위 큐 구현 -> 우선순위가 가장 높은 데이터를 가장 먼저 삭제
#최소힙구조 기반 라이브러리 사용

#(거리,노드)정보 객체를 우선순위 큐에 삽입
#거리순대로 정렬
#즉 최단 거리가 가장 짧은 노드를 선택하는 과정을 우선순위 큐를 이용하는 방법으로 대체

import heapq
import sys
input=sys.stdin.readline()
INF=int(1e9)

n,m=map(int,input().split())
start=map(int,input())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

#간선정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra2(start):
    q=[]
    heapq.heappush(q,(0,start))#시작노드 큐 삽입
    distance[start]=0
    while q: #큐가 비어있지 않는다면
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra2(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("도달불가")
    else:
        print(distance[i])