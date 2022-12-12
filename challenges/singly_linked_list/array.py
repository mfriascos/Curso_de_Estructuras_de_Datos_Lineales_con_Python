
class Array():
    
    def __init__(self, capacity, fill_value = None) -> None:
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        