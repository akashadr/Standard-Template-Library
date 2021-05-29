if __name__=="__main__":
  
  l=list(map(int,input().split(',')))
  
  for i in l:
    
    if(i==l[-1]):
      print(i+1)
    
    else:
      print(i+1,end=', ')