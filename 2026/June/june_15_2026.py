# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        count=0
        while dummy:
            count+=1
            dummy=dummy.next

        temp=head.next
        prev=head

        if count==1:
            return None

        for i in range(count//2-1):
            prev=temp
            temp=temp.next

        prev.next=temp.next if temp else None
        return head


        