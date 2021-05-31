def isSubsequence(s,t):
  N1=len(s)
  N2=len(t)
  
  if(N1>N2): return False

  i = 0
  j = 0
  
  while((i < N1) and (j < N2)):
    if (s[i] == t[j]):
      i +=1
      j +=1
    else:
      j +=1
                
  return i == N1


if __name__=="__main__":
  
  print(isSubsequence("ace","abcde"))
  
  
