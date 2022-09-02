class Node:# this represents each node of the LL
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data

class LinkedList:#class to represent the LinkedList
    def __init__(self, nodes=None):# store where the start of the list begins 'head'
        self.head = None
        #these lines allows to quickly create a linked list with some data
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node 
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    #repr func to have a more helpfull representation of the objects
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        

#method below goes -> list and yields every single node
#remember you always have to validate the current node is not None
#when condition is true you are at end of list 
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
#adding something to the front of the node
    def add_first(self, node):
        node.next = self.head
        self.head = node 

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        
   #create the list     
'''llist = LinkedList()
llist
None

first_node = Node("a")
llist.head = first_node
llist


second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)'''

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)
llist.add_first(Node('hello'))
print(llist)
for node in llist:
    print(node)
newList = LinkedList()
newList.add_first(Node('b'))
print(newList)
