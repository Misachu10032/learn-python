# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        one = list1
        two = list2
        while one or two:
            if not two:
                cur.next = ListNode(one.value)
                one = one.next
                cur = cur.next
            elif not one:
                cur.next = ListNode(two.value)
                two = two.next
                cur = cur.next

            elif one.value > two.vale:
                cur.next = ListNode(two.value)
                two = two.next
                cur = cur.next
            else:
                cur.next = ListNode(one.value)
                one = one.next
                cur = cur.next

        return dummy.next
