#왕실의 나이트
#8*8 좌표 평면 -> 특정한 한칸에 나이트가 있음
#나이트가 이동시에는 L자 형태로만 이동가능 -> 1. 수평으로 두칸 이동, 수직 한칸/ 2. 수직 두칸 수평 한칸
#행 1~8, 열 a~h로 표현

#입력은 a1처럼 열과 행으로 구성
state=input() #나이트 위치
row=int(state[1]) #행
columns=int(ord(state[0])-ord('a')+1) #열 아스키코드 변환 -> 어쨋든 a가 1로 시작해야하니까 아스키코드를 그에 맞게 변환
steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)] #각 나이트가 이동할 수 있는 방향
count=0 #경우의수
for i in range(len(steps)):
    next_x=columns+steps[i][0]
    next_y=row+steps[i][1]
    if  next_y>=1 and next_x>=1 and next_x<9 and next_x<9:
        count+=1
print(count)

