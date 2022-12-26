#카드숫자게임
#룰
# N*M 형태 N: 행의개수, M은 열의개수
# 행 선택 -> 가장 숫자 낮은 카드 뽑기 -> 최종적으로 가장 높은 숫자 카드 뽑기

# 풀이
# 1. 각 행별 정렬해서 작은 숫자 픽  / 2. 픽한 숫자중 큰 숫자 출력
N,M=map(int,input().split())
min_card=[]
for i in range(N):
    card=list(map(int,input().split()))
    min_card.append(min(card))
print(max(min_card))

