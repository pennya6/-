#순차탐색
#앞에서부터 차례대로 확인
#정렬되어있지않은 상태로 사용
def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1

print("문자열입력")
input_data=input().split()
n=int(input_data[0])#원소의 개수
target=input_data[1]

print("문자열입력")
array=input().split()

print(sequential_search(n,target,input_data))