#BFS(너비우선탐색)->큐(선입선출)

#BFS 동작원리
#탐색시작 노드 큐에 삽입 방문처리
# -> 인접노드중 방문하기 않은 노드 모두 큐에 삽입 방문처리
# -> 반복
from collections import deque

def bfs(graph,start,visited):
    queue=deque([start]) # 큐 구현
    visited[start]=True #방문처리

    while queue: #큐에 아무것도 없을때까지 반복
        v=queue.popleft() #큐에서 하나의 원소 뽑아 출력
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]: #방문하지 않았다면
                queue.append(i) #큐에 넣고
                visited[i]=True #방문처리

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph,1,visited)
