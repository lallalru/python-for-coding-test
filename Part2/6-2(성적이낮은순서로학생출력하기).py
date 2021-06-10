n = int(input())
list = []
for i in range(n):
  list.append(input().split() )

list = sorted(list, key=lambda name:name[0])

for i in list:
  print(i[0], end=" ")
