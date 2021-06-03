class Node:

    def __init__(self, data):

        self.data = data

        self.ptr = None  
        

def pairwiseSwap(temp):

  while(temp is not None and temp.ptr is not None):
    if(temp.data != temp.ptr.data):
      temp.data, temp.ptr.data = temp.ptr.data, temp.data
    temp = temp.ptr.ptr

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
 

one.ptr = two

two.ptr = three

three.ptr = four

four.ptr = None


pairwiseSwap(one)

printList(one)