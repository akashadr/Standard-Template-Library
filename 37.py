def Decimal_To_Binary(DN):
  
  if(DN==0 or DN==1):
    
    return DN
  
  else:
    
    BN=""
  
    while(DN>0):
    
      BN=str(DN%2)+BN
   
      DN=DN//2
    
    return int(BN)



if __name__=="__main__":
  
  N = int(input())
  L = list()
  
  for i in range(N+1):
    
    X=Decimal_To_Binary(i)
    Y=str(X).count('1')
    L.append(Y)
  
  print(L)