if __name__=="__main__":
  
  N=int(input())
  Str=""
  
  if(N&1):
    Str+=('a'*N)
    
  else:
    Str+=('a'*(N-1))
    Str+='b'
  
  print(Str)