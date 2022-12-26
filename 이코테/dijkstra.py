#최단경로 알고리즘
#1. 다익스트라 최단경로 알고리즘
# - 특정 노드에서 출발해 다른 노드로 가는 각각 최단 경로 구해줌, 그리디 알고리즘
# 원리 - 출발노드 설정, 최단거리 테이블 초기화, 최단경로가 가장 짧은 노드 선택, 최단거리테이블 갱신신
#2. 플로이드워셜
#3. 벨만 포드 알고리즘

#다익스트라 알고리즘 구현
#1. 간단한 방법
import sys
input=sys.stdin.readline #input을 더 빠르게 동작하는 내장함수
INF=int(1e9) #무한을 의미

#노드수, 간선수
n,m=map(int,input().split())
start=int(input())
graph=[[]for i in range(n+1)] #모든 리스트는 (노드개수+1)크기 할당
visited=[False]*(n+1) #방문체크 리스트
distance=[INF]*(n+1) #최단거리 테이블 무한 초기화

#간선정보 입력
for _ in range(m): #인덱스 무시(_)
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #a번 노드에서 b번 노드로 가는 비용이 c

#방문하지 않은 노드중 가장 최단거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value=INF
    index=0 #가장 최단거리가 짧은 노드
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    distance[start]=0 #시작노드 초기화
    visited[start]=True #시작노드 방문처리
    for j in graph[start]:
        distance[j[0]]=j[1] #j[0]현재노드, j[1]목적지노드
    #시작노드 제외 반복
    for i in range(n-1):
        #현재 최단거리가 가장짧은 노드 반환하여 방문처리
        now=get_smallest_node()
        visited[now]=True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost=distance[now]+j[1]
            #현재노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("도달불가")
    else:
        print(distance[i])