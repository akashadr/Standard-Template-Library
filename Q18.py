if __name__=="__main__":
  
  N=int(input())
  Fac=[]
  
  if(N==0):
    print(Fac)
  
  elif(N==1):
    Fac.append(1)
    print(Fac)
  
  else:
    
    for i in range(2,N//2+1):
    
      if(N%i==0):
        Fac.append(i)
   
    Fac.insert(0,1)
    Fac.append(N)
  
    print(Fac)
  
  