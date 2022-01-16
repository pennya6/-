#떡볶이 떡 만들기
#절단기 높이 H, 손님이 요청한 총 길이 M, 적어도 M만큼 얻기
#접근 : 이진탐색? 잘라서 M보다 작으면  크면 이런식으로?
n,m=list(map(int,input().split()))
rice_length=list(map(int,input().split()))

def binary_search(array,n,m,start):
    end=max(array)
    total=0
    while(start<=end):
        mid=(start+end)//2
        for x in array:
            if x>mid:
                total+=x-mid
        if total<m:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return print(result)

binary_search(rice_length,n,m,0)