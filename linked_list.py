from node import Node

class SinglyLinkedList():
    
    def __init__(self) -> None:
        self.tail = None
        self.size = 0
    
    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current = current.next

            current.next = node
        
        self.size +=1
    
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val                   #*Genera valores pero no los almacena en una estructura de datos, no se
                                        #*quedan en memoria 
    
    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data: 
                if current == self.tail: 
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            
            previous = current
            current = current.next
        
    def search(self, data):
        for node in self.iter():
            if data == node: 
                print(f"Dat {data} found!")
            else: 
                raise ValueError("Data don't found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0