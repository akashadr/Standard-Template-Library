if __name__=="__main__":
  
  N =  [[1, 1, 1],[0, 0, 1],[1, 1, 1]] 



  
  Count=0
  
  for i in range(len(N)):
    for j in range(len(N[0])):
      
      if(N[i][j]==1):
        Count+=1
  
  print(Count)
