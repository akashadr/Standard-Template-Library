if __name__=="__main__":
  
  l=list(map(int,input().split(',')))
  
  Sum=0
  
  for i in range(5):
    
    Max=max(l)
    l.remove(Max)
    Sum+=Max
  
  print(Sum)
  