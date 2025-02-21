class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Calculate the length of the linked list
        length = 0
        l1 = head
        while l1 is not None:
            length += 1
            l1 = l1.next
        # Edge case: removing the head node
        if length == n:
            return head.next
        # Find the (length - n - 1)th node
        i = 0
        l2 = head
        while i < length - n - 1:
            l2 = l2.next
            i += 1
        # Remove the nth node from the end
        l2.next = l2.next.next
        return head