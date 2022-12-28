from node import Node

def run():
    head = None
    for count in range(1,6):
        head = Node(count, head)
    
    while head != None:
        print(head.data)
        head = head.next

if __name__ == "__main__":
    run()