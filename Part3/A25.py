n= int(input())
stages = list(map(int, input().split()))
temp = [0]*(n+1)#스테이지에 도달했으나 아직 못깬 인원수 1~n+1
answer = [0]*(n+1)#return용 0~n+1
count = len(stages)#스테이지별 도달한 인원수
result = [0]*(n)

for i in stages:
  temp[i-1] += 1 

if temp[n-1] == len(stages):
  result =[n for n in range(n)]
  result[0] = n
  print(result)
else:
  for i,v in enumerate(temp) :
    print("temp[",i,"]:",temp[i], " count: ", count)
    if count!=0:
      answer[i] = (i+1,float(temp[i]/count))
    else:
      answer[i] = (i+1,0)
    count -= temp[i]
  print("before:",answer)
  answer.sort( key=lambda x:(-x[1],x[0]) )
  print("after:",answer)

  
  
  if answer[0][0] ==(n+1):
    for i in range(1,n+1):
      print("answer[",i,"][0]:",int(answer[i][0]))
      result[i-1] = int(answer[i][0])
  else:
    for i in range(0,n):
      print("answer[",i,"][0]:",int(answer[i][0]))
      result[i] = int(answer[i][0])

  
  print(result[0:n])
 #=======================
#  def solution(N, stages):
#     temp = [0]*(N+1)#스테이지에 도달했으나 아직 못깬 인원수 1~n+1
#     answer = [0]*(N+1)#return용 0~n+1
#     count = len(stages)#스테이지별 도달한 인원수
#     result = [0]*(N)
    
#     for i in stages:
#         temp[i-1] += 1 
#     if temp[N-1] == len(stages):
#         result =[n for n in range(N)]
#         result[0] = N
#         return result
#     else:
#         for i,v in enumerate(temp) :
#             #print("temp[",i,"]:",temp[i], " count: ", count)
#             if count!=0:
#                 answer[i] = (i+1,float(temp[i]/count))
#             else:
#                 answer[i] = (i+1,0)
#             count -= temp[i]
#         answer.sort( key=lambda x:(-x[1],x[0]) )

#         if answer[0][0] ==(N+1):
#             for i in range(1,N+1):
#                 #print("answer[",i,"][0]:",int(answer[i][0]))
#                 result[i-1] = int(answer[i][0])
#         else:
#             for i in range(0,N):
#                 #print("answer[",i,"][0]:",int(answer[i][0]))
#                 result[i] = int(answer[i][0])
        
#         return result[0:N]
