s = input()

count = result = 0
total = 1
temp = s[0]

for i in range(1,len(s)):
  if temp != s[i]:
    temp = s[i]
    count += 1
    total += 1
  else:
    continue

count = (count+1)//2
result = count if count < total-count else total-count
result = 0 if total==1 and count==0 else result
print(result) 