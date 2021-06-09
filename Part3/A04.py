n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
target = 1

for i, v in enumerate(data):
  if target < v:
    break;
  target += v
print(target)