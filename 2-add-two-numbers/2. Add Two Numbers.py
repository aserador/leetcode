# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        ans = ListNode()
        pwr = 0
        while l1:
            x = l1.val
            n1 += x * (10**pwr)
            pwr += 1
            l1 = l1.next
        pwr = 0
        while l2:
            x = l2.val
            n2 += x * (10**pwr)
            pwr += 1
            l2 = l2.next
        n_sum = n1 + n2
        if n_sum == 0: 
            return ListNode(0)
        curr = ans
        while n_sum > 0:
            curr.next = ListNode(n_sum % 10)
            n_sum = n_sum // 10
            curr = curr.next
        return ans.next
            