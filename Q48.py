import functools

if __name__=="__main__":
  
  L=list(map(int,input().split(',')))
  Result=[]
  
  for i in range(len(L)):
    New=list(L)
    New.remove(L[i])
    Result.append(functools.reduce(lambda a, b: a*b, New))
 
  print(Result)