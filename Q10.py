if __name__=="__main__":
  
  l=list(map(int,input().split(',')))

  for i in l:
    
    if(i&1==0):
       
       if(i==l[-1]):
         print(i)
         
       else:
         print(i,end=", ")