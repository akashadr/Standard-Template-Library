def SortString(s):             
    l = list(s)
    ans = []
    
    while l:
      
       Temp = list(set(l))  
       Temp.sort()  
       for i in Temp:
           ans.append(i)
           l.remove(i)
           
       Temp = list(set(l))
       Temp.sort(reverse=True)
       for i in Temp:
           ans.append(i)
           l.remove(i)
           
    return ''.join(ans)
 
if __name__=="__main__":
  
  S=input()
  print(SortString(S))