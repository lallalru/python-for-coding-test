n = list(map(int,input()))
length = len(n)
half = int(length/2)
left = [n[i] for i in range(0,half)]
right = [n[i] for i in range(half,length)]

if sum(left) == sum(right):
  print("LUCKY")
else:
  print("READY")
