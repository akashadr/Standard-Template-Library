if __name__=="__main__":
  
  L=list(map(str,input().split(',')))
  
  L1=list(map(int,list(L[0].strip())))
  L2=list(map(int,list(L[1].strip())))
  
  if(sum(L1)==sum(L2)):
    print("true")
  else:
    print("false")