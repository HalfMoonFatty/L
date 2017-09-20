"""flatten 4-direction doubly linked list.
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.up = None
    self.down = None
    self.prev = None
    self.next = None

  def __str__(self):
    return str(self.val)


def FlattenToDoublyLinkedList(head):
  if not head:
    return

  tail = head
  while tail.next:
    tail = tail.next

  cur = head
  while cur:
    if cur.up:
      tail.next = cur.up
      cur.up.pre = tail
      while tail.next:
        tail = tail.next
      # Clean up the up/down links.
      cur.up.down = None
      cur.up = None

    if cur.down:
      tail.next = cur.down
      cur.down.pre = tail
      while tail.next:
        tail = tail.next
      # Clean up the up/down links.
      cur.down.up = None
      cur.down = None

    cur = cur.next
