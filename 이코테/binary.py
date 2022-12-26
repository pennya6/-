#이진탐색
#정렬시 사용가능
#찾을려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터 찾기
#구현방법 1)재귀함수 2)반복문

#1)재귀함수 이진탐색
def binary_search1(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search1(array,target,start,mid-1)
    elif array[mid]<target:
        return binary_search1(array,target,mid+1,end)


#2)반복문 이진탐색
def binary_search2(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            start=mid-1
        else:
            start=mid+1
    return None

n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

print(binary_search1(array,target,0,n-1) + 1) #인덱스 0번부터 시작하기 때문
print(binary_search2(array,target,0,n-1)+1)



