import math

class Node:
  def __init__(self,data):
    self.data = data
    self.ptr = None

def Solution(head):
  
  end = one

  counter = 0
  
  while(end.ptr):
    end = end.ptr
    counter +=1
          
  counter = math.ceil(counter/2)   

  temp = one

  while(counter!=0):
    end.ptr = temp.ptr
    temp.ptr = temp.ptr.ptr
    end.ptr.ptr = None
    temp = temp.ptr
    end = end.ptr
  
    counter-=1
  


def printList(temp):
  while(temp):
    if(temp.ptr!=None):
      print(temp.data,'->',end=" ")
    else:
      print(temp.data)
    temp = temp.ptr
  



one = Node(1)

two = Node(2)

three = Node(3)

four = Node(4)

five = Node(5)
 



one.ptr = two

two.ptr = three

three.ptr = four

four.ptr = five

five.ptr = None


  
Solution(one)

printList(one)