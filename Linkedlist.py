Class Node: # Node Class
  def __init__(self,data): #defining a node class object
    self.data=data #assigning data
    self.next=None #assigning next as null

Class Singly LinkedList: # linked list class
  def __init__(self): #defining a linked list object
    self.head==None # initialising head pointer
    
  def insertFront(self,data):
    new_node=Node(data) #creating a new node
    new_node.next=self.head #storing the address of head in new_node next
    self.head=new_node #updating the head
    
  def insertEnd(self,data):
    new_node=Node(data) #creating a new node
    if self.head is None: #if linked list is empty
      self.head=new_node
    else: # if linked list is not empty
      temp=self.head # initialising temp variable
      while temp.next: #looping till temp.next becomes null
        temp = temp.next #updating temp
      temp.next=new_node #appending the new_node
        
  def insertAtPos(self,data):
    
  def insertAfterNode(self,data):
    
  def deleteNode(data):
    
  
if __name__=="main":
  print("Enter the number of function which you want to perform")
  print("1: Insert at Front","2: Insert at End", "3: Insert at Position", "4: Insert after Node", "5: Delete a Node", "6: Reverse the List",
        "8: Print the LinkedList", "9: Exit",sep="\n")
  num=0
  while num!=9:
     num=int(input())
    if num<1 or num>9:
      print("Invalid Input")
    else:
      if num==1:
        print("Enter the data to insert")
        data=int(input())
        insertFront(data)
       
      elif num==2:
        print("Enter the data to insert")
        data=int(input())
        insertEnd(data)
       
      elif num==3:
        print("Enter the data to insert")
        data=int(input())
        insertAtPos(data)
        
      elif num==4:
        print("Enter the data to insert")
        data=int(input())
        insertAfterNode(data)
  
