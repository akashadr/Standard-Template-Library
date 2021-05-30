if __name__=="__main__":
  
  Str=input().lower()
  S=set(Str)
  
  if(len(S)==len(Str)):
    print("true")
  else:
    print("false")