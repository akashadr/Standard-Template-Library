if __name__=="__main__":
  
  Str=input()

  count=0
  l=list()

  for i in Str:
    if (i == "("):
      count=count+1
    elif(i == ")"):
      count=count-1
    
    l.append(count)
  
  
  print(max(l))
   
   