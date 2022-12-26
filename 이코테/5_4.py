#미로탈출
#N*M 크기의 미로, (1,1)위치 동빈, 미로의 출구(N,M), 괴물 있으면 0 없으면 1,
#문제 풀이 -> BFS, 0이면 그 전으로 가서 1이면 다음으로 가기

#Hint
#1. 위치 이동 -> 상하좌우
#2. (x,y) 좌표
#3. 카운트 또는 괴물이 없는 곳이 1인 이유가 있음 -> 그전 값에 +1
from collections import deque

n,m=map(int,input().split())
info=[]
for i in range(n):
    info.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while deque:
        x, y = deque.popleft()
        for i in range(4): #상하좌우
            #갱신 (x,y)
            nx = x + dx[i]
            ny = y + dy[i]
            #경계에 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if info[nx][ny]==0:
                continue
            if info[nx][ny]==1: #그전값에 +1
                info[nx][ny]=info[x][y]+1
                info.append((nx,ny))
    return info[n-1][m-1]

print(bfs(0,0))