class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def __repr__(self):
    return str(self.data)

root = Node(11)
print(root)