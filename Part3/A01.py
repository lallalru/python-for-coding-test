n = input()
m = list(map(int, input().split()))
m.sort()

#count : 여행에 참여하는 인원 수
count = result = 0

for i in m:
  count +=1
  if count >= i:
    result += 1
    count = 0

print(result) 