def MaxSumSubarray(arr):
  
  maxsum = float('-inf')
  currsum = 0
  
  
  for i in range(len(arr)): #Kadane's algorithm
    
    currsum+=arr[i]         #T=O(n)
    
    if(currsum>maxsum):
      
      maxsum = currsum
    
    if(currsum<0):
      
      currsum=0
   
   
  return maxsum


if __name__=="__main__":
  
  L1 = [-3,-2,-1,-4,-5]
  L2 = [5,4,-1,7,8]
  L3 = [-2,1,-3,4,-1,2,1,-5,4]
  
  print(MaxSumSubarray(L1))
  print(MaxSumSubarray(L2))
  print(MaxSumSubarray(L3))