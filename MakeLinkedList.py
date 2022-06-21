class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
 
# Create and Handle list operations
class LinkedList:
    def __init__(self):
        self.head = None # Head of list
  
    # Pushes new data to the head of the list
    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
#%%
# Driver code
linkedList = LinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(2)
linkedList.push(1)
 
print("Given linked list")
print(linkedList)