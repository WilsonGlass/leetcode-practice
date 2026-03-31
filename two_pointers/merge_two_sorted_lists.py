"""
You are given the heads of two sorted linked lists list1 and list2
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val > list2.val:
            cur.next = list2
            list2 = list2.next
        else:
            cur.next = list1
            list1 = list1.next