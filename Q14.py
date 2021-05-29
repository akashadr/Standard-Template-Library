import numpy as np

def BubbleSort(a,n):

   for i in range(1,n):
     
      Swapped = False

      for j in range(0, n - i):
       
          if(a[j]>a[j+1]):
           
             a[j],a[j + 1]=a[j+1],a[j]
             Swapped = True
           
      if(not Swapped):
        break
   
   


def display(a,n):
  for i in range(0,n):
     print(a[i],end=" ")



if __name__=="__main__":
  
  arr=np.array([1,2,10,50,5])
  
  if(len(arr)==0):
    
    print(arr)
       
  BubbleSort(arr, len(arr))
   
  display(arr, len(arr))
 
