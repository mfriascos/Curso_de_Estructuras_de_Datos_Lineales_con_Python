from grid import Grid
from array import Array

class Cube():
    
    def __init__(self, rows, columns, depth, fill_value = None) -> None:
        self.fill = Grid(rows,columns)
        for row in range(rows):
            for col in range(columns):
                self.fill[row][col] = Array(depth, fill_value)

    def __get_rows__(self):
        return self.fill.__get_height__()
    
    def __get_columns__(self):
        return self.fill.__get_width__()
    
    def __get_depth__(self):
        return len(self.fill[0][0])
    
    def __get_item__(self, index):
        return self.fill[index]
    
    def __str__(self):
        result = ""

        for depth in range(self.__get_depth__()):
            result += f'index depth:[{depth}] \n'
            for row in range(self.__get_rows__()):
                for col in range(self.__get_columns__()):
                    result += f'{self.fill[row][col][depth]}'
                    
                result += "\n"
            result += "\n"

        return str(result) 

