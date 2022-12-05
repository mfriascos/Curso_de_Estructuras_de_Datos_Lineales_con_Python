from linked_list import SinglyLinkedList


def run():
    #* To create the object
    words = SinglyLinkedList()

    #*To fill the object
    words.append('Egg')
    words.append('Rice')
    words.append('Coffee')
    words.append('Juice')

    #* To Verify size of list 
    #words.size

    #* To Create an iterable method 
    words.iter()

    #* To Delete a node 
    words.delete('Juice')

    #* To Search an object
    words.search('Rice')
    words.search('Bread')

    #* To clean the list
    words.clear()


if __name__ == '__main__':
    run()