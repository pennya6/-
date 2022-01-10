#정렬알고리즘 -> 선택정렬/삽입정렬/쿽정렬/계수정렬
#1.선택정렬 : 가장 작은것을 선택(앞부분은 정렬됨, 따라서 뒷부분 스와프)
def sort1(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i] #스와프

#삽입정렬 : 정렬되어 있을때 효율적인 정렬, 적절한 위치에 삽입하는 아이디어, 자신보다 작은 아이 만나면 삽입
def sort2(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1): #인덱스 i부터 1까지 감소하는 작업
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break

#퀵정렬 : 피벗을 이용한 정렬, 이미 정렬되어있는 데이터가 아님


array=[7,5,9,0,3,1,6,2,4,8]