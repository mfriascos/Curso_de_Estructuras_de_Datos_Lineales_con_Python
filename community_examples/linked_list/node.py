
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
#*The LinkedList should know the first node and size list

    def append(self,value):
        my_node = Node(value)
        if self.size == 0:
            self.first = my_node
        else:
            current = self.first
            while current.next != None:
                current = current.next

        self.size +=  1

        return my_node
    
    def remove(self, value):
        if self.size == 0: 
            return False
        else:
            current = self.first
            while current.next.value != value:
                if current.next == None:
                    return False
                else:
                    current = current.next
            deleted_node = current.next
            current.next = deleted_node.next
        self.size -= 1

        return deleted_node

    def __len__(self):
        return self.size
    
    def __str__(self):
        string = "["
        current = self.first
        while current != None:
            string += str(current)
            string += str(",")
            current = current.next
        string += "]"

        return string

        

