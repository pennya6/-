#음료수얼려먹기
#세로길이 n,가로길이 m
#접근방법
#DFS->모든 하위가 1이 나오면 다음으로 넘기기 그리고 카운트 세기

#dfs기본 함수
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0: #아직 방문전이면
        graph[x][y]=1 #방문처리
        #상하좌우 살펴보기
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

count=0 #그룹수 세기
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True: #우리가 찾을려고 하는 그룹들이 0이기 때문
            count+=1
print(count)


