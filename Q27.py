def Multiples(Num,length):
  
  l=list()
  
  for i in range(1,length+1):
    
    l.append(Num*i)
  
  return l

if __name__=="__main__":
  
  print(Multiples(17,6))