#DFS(깊이우선탐색)->스택(선입후출)
#그래프 표현방법 -> 1.인접행렬, 2.인접리스트

#인접행렬방법
# INF=999999999
# graph=[
#     [0,7,5],
#     [7,0,INF],
#     [5,INF,0]
# ]
# print(graph)

#인접리스트방법
# graph=[[] for _ in range(3)]
# graph[0].append((1,7))
# graph[0].append((2,5))
# graph[1].append((0,7))
# graph[2].append((0,7))
# print(graph)

#DFS 동작원리
#시작노드를 스택에 삽입 방문처리
# -> 최상단 노드를 기준으로 방문 안한곳 방문 후 방문처리 / 없으면 최상단 꺼냄
# -> 반복
def dfs(graph,v,visited):
    visited[v]=True #현재 방문처리
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]: #방문이 안되어있다면 
            dfs(graph,i,visited) #방문처리하고 재귀
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
visited=[False]*9 #방문처리
dfs(graph,1,visited)

