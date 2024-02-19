# creating linked list node.
class Node:
  def __init__(self, val, next):
    self.val = val
    self.next = next

def printLinkedList(head):
  linkedList = ''
  
  while head:
    linkedList += str(head.val) + ' -> '
    head = head.next
  
  print(linkedList + 'None')


node1 = Node(val=1, next=None)
node2 = Node(val=2, next=None)
node3 = Node(val=3, next=None)
node4 = Node(val=6, next=None)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

printLinkedList(head)

