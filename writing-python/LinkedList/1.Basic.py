from typing import Any

class Node:
  def __init__(self, data: Any):
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self.head = None

  def traverse(self):
    temp = self.head

    while (temp):
      print(temp.data, end=" ")
      temp = temp.next
    print()
  
  def push_back(self, data: any):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

  def push(self, data: any):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    new_node.next = self.head
    self.head = new_node
  
  def remove(self, data: Any):
    prev = None
    curr = self.head

    if curr is not None:
      if curr.data == data:
        self.head = curr.next 
        curr = None
        return
    
    while (curr is not None):
      if curr.data == data:
        break
      prev = curr
      curr = curr.next

    if curr is None:
      return
    
    prev.next = curr.next
    curr = None
      
    
    
linked_list = LinkedList()

node1 = Node(11)
linked_list.head = node1
node2 = Node(12)
node3 = Node(13)

node1.next = node2
node2.next = node3

linked_list.push(10)
linked_list.remove(9)
linked_list.traverse()

