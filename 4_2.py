# 구현 - 시각
# 수 n을 입력해서 00:00:00 ~ n:59:59까지 3 포함인 경우의수 구하기
# 완전탐색 방법

#시각
n=int(input())
#경우의수
count=0
#시간
for i in range(n+1):
    #분
    for j in range(60):
        #초
        for k in range(60):
            # 3이 들어간 경우 찾기
            # 시간을 문자열로 만들어서 문자열에 3이 있니?
            if '3' in str(i)+str(j)+str(k):
                count+=1
print(count)
