# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t_l = []
        t_n = head
        while t_n != None:
            t_l.append(t_n.val)
            if t_n.next == None:
                break
            t_n = t_n.next
        print(t_l)
        if len(t_l) < 2:
            return head
        r_l = [0 for _ in range(len(t_l))]
        for idx, t in enumerate(t_l):
            r_l[(idx+k)%len(t_l)] = t
        c_head = ListNode(r_l[0])
        c_node = c_head
        for r in r_l[1:]:
            t_node = ListNode(r)
            c_node.next = t_node
            c_node = c_node.next
        return c_head