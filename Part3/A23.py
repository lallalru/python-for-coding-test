n = int(input())
score = []
for i in range(n):
  score.append(input().split() )


score = sorted(score, key=lambda name:(-int(name[1]),int(name[2]),-int(name[3]),name[0]) )

for i in score:
  print(i[0])