"""
I feel like I don't truly understand this one. I should try and come back to this.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Order the linked list such that
    [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]
    """
    if not head:
        return

    # Find middle and end
    fast, slow = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Step 2: Reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        nextt = curr.next # temp variable
        curr.next = prev # change the pointer
        prev = curr # setup for next iter
        curr = nextt # setup for next iter

    # Step 3: merge
    h1 = head # first num e.g. 1
    h2 = prev # last num e.g. 5
    while h2:
        nextt = h1.next
        h1.next = h2
        h1 = h2
        h2 = nextt

