from node import Node


def run():
    print(
        '''
        ***** MANUAL FORM *****
        ''')
    
    node3 = Node("C", None)
    node2 = Node("B", node3)
    node1 = Node("A", node2)

    print(f"node 1: {node1}",f"node 2: {node2}",f"node 3: {node3}", sep="\n")

    print(
        """
        ***** ITERATIVE FORM *****
        """)

    head = None

    for count in range(1,6):
        head = Node(count, head)

    node_number = 1

    while head != None:
        print(f"Node {node_number}: {head}", f"node data {node_number}: {head.data}")
        head = head.next
        node_number += 1


if __name__ == "__main__":
    run()