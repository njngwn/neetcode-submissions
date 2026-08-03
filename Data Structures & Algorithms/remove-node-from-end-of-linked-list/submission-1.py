# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # remove the node
        node = dummy = ListNode(0, head)
        for _ in range(length-n):
            node = node.next
        node.next = node.next.next

        return dummy.next
