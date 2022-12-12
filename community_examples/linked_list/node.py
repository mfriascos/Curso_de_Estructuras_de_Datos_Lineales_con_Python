
class Node:

    def __init__(self,value) -> None:   #*Each node has a value!
        self.value = value
        self.next = None

    def __str__(self) -> str:           #*Return the value in string 
        return str(self.value)
    

class LinkedList:

    def __init__(self):                 
        self.first = None               #*Information about the list, the first node
        self.size = 0                   #*Size list 

    def append(self,value):
        my_node = Node(value)
        if self.size == 0:
            self.first = my_node
        else:
            current = self.first
            while current.next != None:
                current = current.next
