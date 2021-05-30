def repdigit(N):
  
  if(N>0 and len(str(N))>=2):
    N=str(N)
    C=N.count(N[0])
    if(C==len(N)):
      return "true"
    else:
      return "false"
   
  elif(N==0):
    return "true"
   
  else:
    return "false"


if __name__=="__main__":
  
  print(repdigit(int(input())))