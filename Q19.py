if __name__=="__main__":
  
  l=list(map(int,input().split(',')))
  
  N=int(input())
  flag=0
  
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      
      if((l[i]+l[j])==N):
        flag=1
        print('true')
        break

    if(flag==1):
      break
        
  
  else:
    print('false')