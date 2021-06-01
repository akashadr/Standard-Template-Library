L=[[1,0,0,0],[0,5,0,2],[3,0,0,0],[0,0,4,0]]
L1=[[1,0,0],[0,5,0],[0,0,0],[0,0,6]]


print("Row Column Value")

for i in range(len(L)):
  for j in range(len(L[i])):
    
    if(L[i][j]!=0):
       print(f"{i}      {j}     {L[i][j]}")
    