if __name__=="__main__":
  
  L=["samuel", "MABELLE", "letitia", "meridith"]
  
  for i in range(len(L)):
    L[i]=L[i].lower()
    item=L[i].replace(L[i][0],chr(ord(L[i][0])-32),1)
    #item=L[i].capitalize() #We Can Use this also
    L[i]=item
  
  print(L)