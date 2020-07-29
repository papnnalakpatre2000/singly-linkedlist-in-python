class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head=None
        self.count=0
    def length(self):
        curr=self.head
        if self.head is None:
            self.count=0
            return self.count
            
        while True:
                if curr.next==None:
                    self.count+=1
                    return self.count
                    
                    
                curr=curr.next
                self.count+=1
        

        
    def iposition(self,newnode,n):
        z=self.count
        if z+2 < n or n==0:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Entered no should be grater than 0 and  less than ", z+2)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            return
            
        if self.head == None :
            self.head=newnode
        else:
            currentnode=self.head
            position=1
            while True:
                if n==1:
                    newnode.next=currentnode
                    self.head=newnode
                    break
                if position == n:
                    prev.next = newnode
                    newnode.next=currentnode
                    break
                prev=currentnode
                currentnode=currentnode.next
                position+=1

    def istart(self,newnode):
        linkedlist1.iposition(newnode,1)

    def iend(self,newnode):
        curr=self.head
        self.count=0

        if self.head == None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            print("Linked list is empty.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            return
        
        linkedlist1.iposition(newnode,linkedlist1.length()+1)
        

    def dstart(self):
        if self.head == None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            print("Linked list is empty.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            return

        curr=self.head
        self.head=curr.next

    def dend(self):
        if self.head == None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            print("Linked list is empty.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            return

        curr=self.head
        c=1
        while True:
            if self.count-1==c:
                curr.next=None
                break
            curr=curr.next
            c+=1


    def dposition(self,n):
        if linkedlist1.length()+2 < n:
            print("Delete position should be greaterthan 0 and less than ",linkedlist1.length()+2)  
            return
        if self.head == None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            print("Linked list is empty.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-----")
            return
        else:
            if n==1:
                curr=self.head
                self.head=curr.next
                return
            else:
                curr=self.head
                position=1
                while True:
                    if position==n:
                        prev.next=current.next
                        break
                    prev=curr
                    curr=curr.next

                
        


    def display(self):
        if self.head is None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Empty linkedlist")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            return
        currentnode=self.head
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        while True:
            
            print(currentnode.data)
            if currentnode.next is None:
                break
        
            currentnode=currentnode.next
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        
    
linkedlist1=Linkedlist()

while True:
    print("---------------MENU---------------")
    print("A> Enter 1 For Insert at Position: ")
    print("B> Enter 2 For Insert at End:")
    print("C> Enter 3 For Insert at Start:")
    print("D> Enter 4 For Delete the Starting Node:")
    print("E> Enter 5 For delete the end node:")
    print("F> Enter 6 For delete the node at given Position:")
    print("G> Enter 7 For Display:")
    print("H> Enter 8 For Display The no of Nodes in linkedList: ")
    print("I> Enter 0 For Exit:")
    print("-----------------------------------------------------")
    
    i=int(input("Enter the Option from Above Menu: "))

    if i==1:
        linkedlist1.iposition(Node(input("Enter the Input:")),int(input("Enter the position:")))
    if i==2:
        linkedlist1.iend(Node(input("Enter the Input:")))
    if i==3:
        linkedlist1.istart(Node(input("Enter the Input:")))
    if i==4:
        linkedlist1.dstart()

    if i==5:
        linkedlist1.dend()

    if i==6:
        linkedlist1.dposition(int(input("Enter the position:")))
    if i==7:
        linkedlist1.display()
    if i==8:
        print(linkedlist1.length())
        
    if i==0:
        break



