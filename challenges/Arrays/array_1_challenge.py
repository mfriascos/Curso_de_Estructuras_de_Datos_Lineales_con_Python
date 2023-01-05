import random
import functools

class Array: 
    def __init__(self, capacity, fill_value=None) -> None:  #* En el método constructor definimos sus atributos como su capacidad o su tamaño. 
        self.items = list()                                 #* los elementos se guardarán en una lista vacía
        for i in range(capacity): 
            self.items.append(fill_value)

    def __len__(self):                                      #* Obtenemos la longitud de la lista self.items
        return len(self.items)
    
    def __str__(self) -> str:                               #* Retorna la expresión en String de self.items
        return str(self.items)
    
    def __iter__(self):                                     #* Crear iterables. 
        return iter(self.items) 

    def __getitem__(self, index):                           #* Método para obtener elementos de acuerdo a una posición 
        return self.items[index]

    def __setitem__(self, index, new_item):                 #* Agregar elementos al array 
        self.items[index] = new_item

    def __random__(self):
        for i in range(len(self.items)):
            self.items[i] = random.randint(0,10)
        
        return self.items
    
    def __sequence__(self):
        first = int(input("Type a initial number -> "))
        for i in range(len(self.items)):
            self.items[i] = first
            first += 1

        return self.items

    def __sum__(self):
        return functools.reduce(lambda a,b : a+b, self.items)
        