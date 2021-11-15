#구현 - 상하좌우
n=int(input())
x,y=1,1
way=input().split()

#좌표같은 문제 처리 방법
dx=[0,0,-1,1]
dy=[-1,1,0,0]
type=['L','R','U','D']

for plan in way:
    for i in range(len(type)):
        if plan==type[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)

