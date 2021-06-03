class Node:

    def __init__(self,data):

        self.data = data

        self.ptr = None

         

def isPalindrome(head):


    Temp = head
 

    stack = []

 

    while Temp != None:

        stack.append(Temp.data)

        Temp = Temp.ptr
 

    while head != None:
 

        i = stack.pop()

         
        if head.data == i:

            ispalindrome = True

        else:

            ispalindrome = False

            break
 

        head = head.ptr

         

    return ispalindrome
 

one = Node(1)

two = Node(2)

three = Node(3)

four = Node(2)

five = Node(1)
 



one.ptr = two

two.ptr = three

three.ptr = four

four.ptr = five

five.ptr = None



result = isPalindrome(one)
 

print(result)