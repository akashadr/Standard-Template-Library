if __name__=="__main__":
  
  N=list(map(int,input().split(',')))
  l=[]
  
  for i in N:
    
    if(i&1==0):
      l.append(i)
   
  print(l)