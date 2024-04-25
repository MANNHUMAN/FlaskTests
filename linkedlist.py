class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is new_node:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        position=0
        if position==index:
            self.insertAtBegin(data)
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print('Index not present')

    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self,index):
        if index>=self.length():
            print("ERROR:'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while cur_node!=None:
            cur_node=cur_node.next
            if cur_idx==index:
                return cur_node.data
            cur_idx+=1

    def erase(self,index):
        if index>=self.length():
            print('ERROR: "Erase" Index out of range!')
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1

my_list=linked_list()
my_list.append(2)
my_list.append(5)
my_list.append(3)
my_list.append(17)
my_list.append(24)
my_list.append(1)

my_list.erase(4)

my_list.display()

print('Element @ 2nd index: %d'%my_list.get(2))