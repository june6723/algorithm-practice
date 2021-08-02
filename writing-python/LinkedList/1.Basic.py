from typing import Any

class Node:
  def __init__(self, data: Any):
    self.data = data
    self.next = None

node = Node(3)
print(f'{node.data}')