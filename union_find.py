#서로소 집합 자료구조는 union과 find 2개의 연산으로 조작가능
#union 합집합 - 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
#find연산 - 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

#union-find 자료구조 = 서로소 집합 자료구조
#트리자료 구조 이용하여 집합 표현 -> 1.union 확인하여 서로 연결된 노드 a,b 확인 1.1 루트노드 찾기 1.2 a`를 b`의 부모노드로 설정
# / 2.모든 union 연산을 처리할때 까지 1번 반복

def find_parent(parent,x):
    if parent[x]!=x: #루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
        return find_parent(parent,parent[x])
    return x

#두 원소가 속한 집합합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#경로 압축 기법 소스코드
def find_parent2(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent2(parent,parent[x])
    return parent[x]

#노드의 개수와 간선의 개수 입력받기
v,e=map(int,input().split())
parent=[0]*(v+1) #부모테이블초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#union 연산을 각각 수행
for i in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end='')

print()

#부모테이블 내용 출력
print('부모테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end='')
