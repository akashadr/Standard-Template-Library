def Convert(N):
  
  N=str(N)
  S=""
  
  L=[int(i)**2 for i in N]
  
  for i in L:
    
    S = S+str(i)

  return int(S)



if __name__=="__main__":
  
  N = int(input())
  
  print(Convert(N))