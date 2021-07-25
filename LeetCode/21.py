class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 : return l2
        if not l2 : return l1

        sumList = []

        if l1:
            while l1.next:
                sumList.append(l1.val)
                l1 = l1.next
            sumList.append(l1.val)

        if l2:
            while l2.next:
                sumList.append(l2.val)
                l2 = l2.next
            sumList.append(l2.val)

        sumList.sort()

        head = ListNode(sumList.pop(0))
        curr = head

        while sumList:
            curr.next = ListNode(sumList.pop(0))
            curr = curr.next

        return head