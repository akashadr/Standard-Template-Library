if __name__=="__main__":
  
  arr=[[-34, -54, -74],[-32, -2, -65],[-54, 7, -43]]
  L=[]
  
  for i in range(len(arr)):
    Max=float('-inf')
    for j in range(len(arr[i])):
      if(arr[i][j]>Max):
        Max=arr[i][j]
    L.append(Max)
  print(L)