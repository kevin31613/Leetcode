class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev