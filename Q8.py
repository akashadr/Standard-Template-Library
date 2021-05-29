def Modify(l,K):
  
  for i in range(1,K+1):
    Min=min(l)
    if(Min<0):
      Ind=l.index(Min)
      l[Ind]=abs(Min)
 


if __name__=="__main__":
  
  l=list(map(int,input().split(',')))
  
  K=int(input())
  
  N=[i for i in l if i <0]
  NegNo=len(N)
  
  if(K<=NegNo):
    
    Modify(l,K)
      
  else:
    
    Rem=K-NegNo
    Modify(l,NegNo)
    
    if(Rem&1):
      
      Min=min(l)
      Ind=l.index(Min)
      l[Ind]=Min-2*Min
  
  
  print(sum(l))
    