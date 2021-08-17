from typing import List

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
def traverse(head: Node):
  temp = head

  while (temp):
    print(temp.val, end=" ")
    temp = temp.next
  print()

def put_into_stack(head: Node) -> List:
  curr = head
  stack = []
  while (curr is not None):
    stack.append(curr.val)
    curr = curr.next
  return stack

def add_with_stack(l1: Node, l2: Node) -> Node:
  s1 = put_into_stack(l1)
  s2 = put_into_stack(l2)
  nextNode = None
  carry = 0

  while s1 or s2:
    num1 = s1.pop() if s1 else 0
    num2 = s2.pop() if s2 else 0

    carry, num = divmod(num1 + num2 + carry, 10)

    node = Node(num)
    if nextNode == None:
      nextNode = node
    else:
      temp = nextNode
      nextNode = node
      node.next = temp
    
  if carry != 0:
    node = Node(carry)
    temp = nextNode
    nextNode = node
    node.next = temp
  return nextNode
  
  # while (True):
  #   result = curr1 + curr2 + carry
  #   if result > 9:
  #     carry = 1
  #     result = result % 10
  #   else:
  #     carry = 0
  #   newNode = Node(result)
  #   newNode.next = nextNode
  #   nextNode = newNode

  #   if len(s1) == 0 and len(s2) == 0:
  #     return newNode
  #   if len(s1) > 0:
  #     curr1 = s1.pop()
  #   else:
  #     curr1 = 0
  #   if len(s2) > 0:
  #     curr2 = s2.pop()
  #   else:
  #     curr2 = 0
    

node_a3 = Node(3, None)
node_a2 = Node(2, node_a3)
node_a1 = Node(9, node_a2)

node_b3 = Node(3, None)
node_b2 = Node(2, node_b3)
node_b1 = Node(9, node_b2)

res = add_with_stack(node_a1,node_b1)
traverse(res)