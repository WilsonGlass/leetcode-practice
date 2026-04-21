"""
Reverse a linked list.
Example to work my head around this:

__start__
prev = None
curr = node(1)

None    [1] -> [2] -> [3] -> None
        ^curr

__iteration_1__
next_temp = node(2)      # save where we're going
node(1).next = None      # flip the pointer backward
prev = node(1)
curr = node(2)

None <- [1]    [2] -> [3] -> None
        ^prev  ^curr

__iteration_2__
next_temp = node(3)
node(2).next = node(1)   # flip backward
prev = node(2)
curr = node(3)

None <- [1] <- [2]    [3] -> None
               ^prev  ^curr

__iteration_3__
next_temp = None
node(3).next = node(2)   # flip backward
prev = node(3)
curr = None              # loop ends here

None <- [1] <- [2] <- [3]
                      ^prev  (new head)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    This is really simple, but I need to memorize this.
    """
    prev = None
    curr = head
    # Starts with curr.next and then everything is equal to one in front of itself.
    # It kind of rotates.
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev