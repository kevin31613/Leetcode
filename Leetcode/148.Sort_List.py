import random
class ListNode:  
    def __init__(self,x):  
        self.val=x
        self.next=None
    def sortList(self,head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if len(head) <= 1:
                return head

            pivot = random.choice(head)
            lt = [v for v in head if v < pivot]
            eq = [v for v in head if v == pivot]
            gt = [v for v in head if v > pivot]

            return self.sortList(lt) + eq + self.sortList(gt)
head = [-1,5,3,4,0]
h = ListNode(head)
print(h.sortList(head))