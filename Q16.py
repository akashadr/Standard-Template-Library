if __name__=="__main__":
  
  Pos,Neg=0,0
  
  Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
  
  if(len(Num)==0):
    
    print(Num)
  
  else:
    for i in Num:
    
      if(i>0):
      
        Pos+=1
    
      elif(i<0):
      
        Neg+=i
  
    Num.clear()
  
    Num.append(Pos)
    Num.append(Neg)
  
    print(Num)