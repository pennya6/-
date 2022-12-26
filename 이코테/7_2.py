#부품찾기문제
#N개의 부품존재, m개의종류 대량구매
#접근 방법 : 이진탐색으로 찾기
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return 'yes'
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    elif array[mid]<target:
        return binary_search(array,target,mid+1,end)


n=int(input())
stock_array=list(map(int,input().split())) #재고
stock_array.sort()
m=int(input())
find_array=list(map(int,input().split())) #손님 찾는 물품
for i in find_array:
    result=binary_search(stock_array,i,0,n-1)
    if result=='yes':
        print('yes')
    else:
        print('no')



