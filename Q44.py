if __name__=="__main__":
  
  L=list(map(int,input().split(',')))
  R=[]
  
  R.append(L[0]*L[1])
  
  for i in range(1,len(L)-1):
    M=L[i-1]*L[i+1]
    R.append(M)
  
  R.append(L[-1]*L[-2])
  
  print(R)