#1로 만들기
x=int(input())
count=0
# while x>=1:
#     if x==1:
#         print(count)
#     if x%5==0:
#         x=x/5
#         count+=1
#     elif x%3==0:
#         x/=3
#         count += 1
#     elif x%2==0:
#         x/=2
#         count += 1
#     else:
#         x-=1
#         count += 1

new_x=1
#보텀업 방식 사용
while new_x<=x:
    if new_x==x:
        print(count)
        break
    if new_x*5!=x and new_x*5<x:
        new_x*=5
        count+=1
    elif new_x*3!=x and new_x*3<x:
        new_x*=3
        count += 1
    elif new_x*2!=x and new_x*3<x:
        new_x*=2
        count += 1
    elif new_x+1!=x and new_x+1<x:
        new_x+=1
        count += 1
