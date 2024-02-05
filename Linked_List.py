class Node:

    def __init__(self, value = None, name=0, next = None, links=None):
        '''значение, имя,  след, линки'''
        if links is None:
            links = []
        self.value = value
        self.t_value = value
        self.next = next
        self.links = links
        self.t_links = links
        self.name = name

class LinkedList:
    def __init__(self):
        self.head = None


    def add_node(self, new_value, name):

        new_node = Node(new_value, name, None, None, )
        if self.head is None:
            self.head = new_node
            return self.head

        next_node = self.head
        while next_node.next:
            next_node = next_node.next
        next_node.next = new_node
        return next_node.next

    def add_link(self, name, new_value):

        '''передать узел и значение привязанного'''

        next_node=self.head

        while next_node:
            if next_node.name == name:
                next_node.links.append(new_value)
                return



            next_node=next_node.next







    def print_list(self):

        next_node = self.head

        while next_node.next:
            print(next_node.value)
            for link in next_node.links:
                if link != None:
                    print(' - ', link)
            next_node = next_node.next
        print(next_node.value)


        for link in next_node.links:
            if link != None:
                print(' - ', link)
