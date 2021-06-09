n = int(input())
m = list(map(int, input().split()))

#볼링공의 무게당 개수를 나타낼 변수
#무게는 1부터 10까지 존재
ball_count = [0] * 10 
result = 0

#볼링공 무게당 개수를 더해준다
for i in m: 
  ball_count[i] += 1

#동일 무게를 제외한 공과 동일 무게 개수를 곱하여 합을 구한다
for i in range(0,10): 
  n -= ball_count[i]
  result += ball_count[i] * n


#O(n^2) 
#하나하나 비교해서 무게가 다른것의 개수를 더하는 방법
# for i in range(0,int(n)-1):
#   for j in range(1+i,int(n)):
#     if m[i] != m[j]:
#       result += 1


print(result) 