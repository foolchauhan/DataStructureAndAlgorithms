# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head): 
    slowPtr = head
    fastPtr = head
    if head is not None:
        while(fastPtr is not None and fastPtr.next is not None):
            fastPtr=fastPtr.next.next
            slowPtr=slowPtr.next
        return slowPtr

