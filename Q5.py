if __name__=="__main__":
  
  l=list(map(int,input().split(',')))
  
  even=list()
  odd=list()
  
  for i in l:
    if(i&1):
      odd.append(i)
    else:
      even.append(i)
  
  
  if(len(even)>len(odd)):
    print(odd[0])
  else:
    print(even[0])