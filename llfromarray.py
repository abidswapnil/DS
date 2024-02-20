# Constructing linked list node.
class Node:
  def __init__(self, val, next):
    self.val = val
    self.next = next


def linkedListBuilder(arr: list) -> str:
  head = None  # This is the head node, which is null at first.
  prev_node = None  # 'prev_node' is keeping track the previous node.
  
  while arr:
    '''
    Creating new node in every iteration.
    This takes the value as the first element
    from the list and set next pointer to None.
    '''
    node = Node(val=arr.pop(0), next=None)
    
    if not head: head = node  # Since, at first head node is always null, so we put the first node in head.
    else: prev_node.next = node  # when we already have the head node, now we will keep track of the previous node.
    
    prev_node = node  # after an iteration 'prev_node' is storing the current node.
  
  '''
  To check the all linked list element let's loop through it.
  '''
  
  linkedList = ''
  
  while head:
    linkedList += str(head.val) + ' -> '
    head = head.next
  
  return linkedList + 'None'  # adding None because while loop ends when head got out of the linked list.


print(linkedListBuilder(arr=[1, 2, 3, 4, 5]))
