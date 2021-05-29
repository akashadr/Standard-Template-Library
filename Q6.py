if __name__=="__main__":
  
  a=int(input("first="))
  d=int(input("diff="))
  n=int(input("n="))
  
  for i in range(0,n):
    if(i==n-1):
      print(a+d*i)
    else:
      print(a+d*i,end=', ')