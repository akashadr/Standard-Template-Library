def Check(S):
  
   if(65<=ord(S[0])<=90 and S[-1]=='.' and S.count("  ")==0 ):
    
     for i in range(1,len(S)-1):
       if(S[i].isupper()==True):
         return False
     return True
   return False
  

if __name__=="__main__":
  
  S = input()
  print(Check(S))
  
 
        