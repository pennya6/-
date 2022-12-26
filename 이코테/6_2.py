#위에서 아래로
#내림차순 정렬
#n: 수의개수
n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))
array.sort(reverse=True)
print(array)