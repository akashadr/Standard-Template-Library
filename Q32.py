if __name__=="__main__":
  
  arr=list(map(int,input().split(',')))
  L=[]
  
  for i in arr:
    
    if(i not in L):
      L.append(i)
      
  L.sort()
  print(L)