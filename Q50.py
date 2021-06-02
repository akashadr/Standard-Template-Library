if __name__=="__main__":
  A = [[1, 2, 3, 4, 5 ],
       [16,17,18,19,6 ],
       [15,24,25,20,7 ],
       [14,23,22,21,8 ],
       [13,12,11,10,9]]

  
  T=0
  B=len(A)-1
  L=0
  R=len(A[0])-1
  Dir=0
  Ans=[]
    
  while(T<=B and L<=R):
    
    if(Dir==0):
      
      for i in range(L,R+1):
        Ans.append(A[T][i])
      T+=1
        
    elif(Dir==1):
      
      for i in range(T,B+1):
        Ans.append(A[i][R])
      R-=1
      
    elif(Dir==2):
      
      for i in range(R,L-1,-1):
        Ans.append(A[B][i])
      B-=1
        
    elif(Dir==3):
      
      for i in range(B,T-1,-1):
        Ans.append(A[i][L])
      L+=1
        
    Dir=(Dir+1)%4
    
  print(Ans)
