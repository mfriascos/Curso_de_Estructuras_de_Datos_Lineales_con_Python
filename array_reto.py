import random
import functools

class Array:
    def __init__(self, capacity, fill_value = None) -> None:
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
    
    def __random__(self):
        self.items = [random.randint(0, self.__len__()) for i in range(self.__len__())]
        return self.items
    
    def __sequency__(self,x):
        self.items = [x+i for i in range(self.__len__())]
        return self.items

    def __reduce_self__(self):
        return functools.reduce(lambda x,y:x+y,self.items)

