from array import Array
import random

class Grid():
    def __init__(self, rows, columns, fill_value = None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    
    def __get_height__(self):
        return len(self.data)
    
    def __get_width__(self):
        return len(self.data[0])
    
    def __getitem__(self,index):
        return self.data[index]

    def __str__(self) -> str:
        result = ""

        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                result += str(self.data[row][col]) + " "
            result += "\n"
            
        
        return str(result)
    
    def __random__(self):
        
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                self.data[row][col] = random.randint(0,10)
    
    def __sequency__(self,x):
        for row in range(self.__get_height__()):
            for col in range(self.__get_width__()):
                self.data[row][col] = x + col + row
            
            x +=(self.__get_width__()-1)
    