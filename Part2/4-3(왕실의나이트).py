position = input()
x = int(ord(position[0])) - 97 +1 #a=97
y = int(position[1])
count = 0 

move = [(2,1),(2,-1),(-2,1),(-2,1)
,(1,2),(1,-2),(-1,2),(-1,2)]

for i in move:
  afterX = x +i[0]
  afterY = y +i[1]
  if afterX>=1 and afterX<=8 and afterY >=1 and afterY<=8:
    count += 1
    #print("i:",i,"x:",x,"y:",y,"afterX:",afterX,"afterY:",afterY)

print(count)