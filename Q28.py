if __name__=="__main__":
  
  N = input()
  
  C = N.count('1')
  
  if(C&1):
    
    N=N+str(1)
    
  else:
    
    N=N+str(0)
  
  print(N)