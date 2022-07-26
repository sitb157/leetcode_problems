# Definition for singly-linked list.
import copy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lists = []
        current = head
        lists.append(current.val)
        while (current.next != None):
            current = current.next
            lists.append(current.val)
            
        print(lists)
        l_lists = len(lists)
        if (l_lists - n) == 0:
            if l_lists == 1:
                return ListNode().next
        first_insert = False
        for i, i_n in enumerate(lists):
            if i != (len(lists) - n):
                if not first_insert:
                    r_head = ListNode(i_n)
                    current_node = r_head
                    first_insert = True
                else:
                    new_node = ListNode(val=i_n)
                    current_node.next = new_node
                    current_node = current_node.next
                print(i_n)
        return r_head