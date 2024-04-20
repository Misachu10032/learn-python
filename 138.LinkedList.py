
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer = head

        while pointer:
            oldNext = pointer.next
            pointer.next = Node(pointer.value, oldNext, none)
            pointer = oldNext

        pointer = head
        while pointer:
            if pointer.random:
                pointer.next.random = pointer.random.next
                pointer = pointer.next.next

        oldList = oldPointer = head
        newList = newPointer = head.next

        while oldPointer:
            oldNext.next = oldList.next.next
            newList.next = newList.next.next if newList.next else None
            oldPointer = oldPointer.next
            newPointer = newPointer.next

        return newList
