class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def hasCycle(head: Node) -> bool:
  outer = head
  node_cnt = 0

  while (outer != None and outer.next != None):
    outer = outer.next
    node_cnt += 1

    visit = node_cnt
    inner = head

    matched = 0
    while (visit > 0):
      if outer != inner:
        inner = inner.next
      if outer == inner:
        matched += 1
        print(inner, outer)
      if matched == 2:
        return True
      visit -= 1
  return False

def hasCycle_hashmap(head: Node) -> bool:
  curr = head
  hashmap = set([])
  if curr is None or curr.next is None:
    return False
  
  while curr is not None:
    if curr in hashmap:
      return True
    else:
      hashmap.add(curr)
    curr = curr.next
  return False
def hasCycle_fast_slow(head: Node) -> bool:
  slow = head
  fast = head

  while (slow is not None and fast is not None):
    slow = slow.next
    fast = fast.next
    if fast is not None:
      fast = fast.next
    if slow is fast:
      return True
    
  return False

node4 = Node(4, None)
node3 = Node(3, node4)
node2= Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)
# node4.next = node0

print(hasCycle_fast_slow(node0))
