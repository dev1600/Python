class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        node=Node(data)
        itr=self.head
        if itr is None:
            self.head=node
            return 
        
        while itr.next is not None:
            itr=itr.next
        
        itr.next=node
    
    def insert_values(self,data):
        
        for item in data:
            self.insert_at_end(item)
    
    def get_length(self):
        l=0
        itr=self.head
        while itr is not None:
            itr=itr.next
            l=l+1
        return l

    
    def remove_at(self,index):
        if self.get_length()-index < 0:
            print("INVALID INDEX NO.")
            return 
        
        if index==1:
            self.head=self.head.next
            return 
            
        itr=self.head
        for i in range(index-2):
            itr=itr.next
            i+=1
        
        # print("Element removed is ", itr.next.data)
        
        temp=itr.next
        itr.next=temp.next
        temp.next=None
            
    def print(self):
        if self.head is None:
            print("Linked List is empty !")
            return 
        
        itr=self.head
        
        while itr is not None:
            print(itr.data)
            itr=itr.next
    
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_end(60)
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.insert_values(['a','b','c'])
    ll.insert_at_end(50)
    ll.remove_at(2)
    print("Length of the linked list is",ll.get_length())
    ll.print()
        