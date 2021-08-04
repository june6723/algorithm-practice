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

  def remove_node(self, node: Node):
    if node == None:
      return

    next_node = node.next
    if next_node is None:
      node = None
      return

    node.data = next_node.data
    node.next = next_node.data
    next_node = None

  def reverse(self):
    if self.head is None:
      return
    prev = None
    curr = self.head
    next = None

    while (curr is not None):
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.head = prev
    
    
linked_list = LinkedList()
# linked_list.push_back(10)
# linked_list.push_back(11)
linked_list.push_back(12)
linked_list.reverse()
linked_list.traverse()

