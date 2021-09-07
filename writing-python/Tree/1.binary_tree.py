class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def __repr__(self):
    return str(self.data)

class BinarySearchTree:
  def __init__(self):
    self.__root = None
  
  def create_bst(self, nodes_list):
    nodes = [None if item is None else Node(item) for item in nodes_list]
    # root nodes
    self.__root = nodes[0]

    for index in range(1, len(nodes)):
      node = nodes[index]

      if node is not None:
        parent_index = (index - 1) // 2
        parent = nodes[parent_index]
        if parent is None:
          raise ValueError(
            f'Missing parent node at index {parent_index},'
            f'Node({node.data})'
          )
        if index % 2 == True:
          parent.left = node
        else:
          parent.right = node

  def insert(self, data, method='iterative'):
    if method in 'recursion':
      self.__root = self._insert_rec(self.__root, data)
    else:
      self._insert_iter(data)

  def _insert_rec(self, node, data):
    if not node:
      node = Node(data)
    else:
      if node.data > data:
        node.left = self._insert_rec(node.left, data)
      else:
        node.right = self._insert_rec(node.right, data)
    return node

  def _insert_iter(self, data):
    # root is None
    if not self.__root:
      self.__root = Node(data)
      return
    
    # create new node
    new_node = Node(data)

    curr = self.__root
    parent = None

    while (curr != None):
      parent = curr
      if curr.data > data:
        curr = curr.left
      else:
        curr = curr.right
    
    if parent.data > data :
      parent.left = new_node
    else:
      parent.right = new_node

  def inorder_traverse(self):
    result = []
    self._inorder_rec(self.__root, result)
    return result

  def _inorder_rec(self, node: Node, result):
    if node == None:
      return
    self._inorder_rec(node.left, result)
    result.append(node.data)
    self._inorder_rec(node.right, result)

  def find_min_node(self, node: Node):
    while node.left:
      node = node.left
    return node
  
  def delete(self, data):
    self._delete_data(self.__root, data)
    
  def _delete_data(self, node: Node, data):
    parent = None
    curr = node
    # Search 
    while curr and curr.data != data:
      parent = curr
      if curr.data < data:
        curr = curr.right
      else:
        curr = curr.left  
    if curr == None:
      return node
    # 1. Leaf node 일 경우
    if curr.left == None and curr.right == None:
      if curr != node:
        if parent.left == curr:
          parent.left = None
        else:
          parent.right = None
      else:
        node = None
    # 2. 자식 노드가 2개 일 경우
    elif curr.left and curr.right:
      min_node_in_right_tree = self.find_min_node(curr.right)
      min_data = min_node_in_right_tree.data
      self._delete_data(node, min_data)
      curr.data = min_data
    # 3. 자식 노드가 1개 일 경우
    else:
      if curr.left:
        child = curr.left
        if parent.left == curr:
          parent.left = child
        else:
          parent.right = child
      else :
        child = curr.right
        if parent.left == curr:
          parent.left = child
        else:
          parent.right = child
    return node

bst = BinarySearchTree()

input_datas = []
for item in input().split(' '):
  if item == 'N':
    input_datas.append(None)
  else:
    input_datas.append(int(item))

bst.create_bst(input_datas)
print(bst.inorder_traverse())