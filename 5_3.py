#음료수얼려먹기
#세로길이 n,가로길이 m
#접근방법
#DFS->모든 하위가 1이 나오면 다음으로 넘기기 그리고 카운트 세기

#dfs기본 함수
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n,m=map(int,input().split())
graph=[]
visited=[False]*n
for i in range(n):
    graph.append(list(map(int,input())))
dfs(graph,0,visited)


