# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        c_node = head
        n_l = []
        while c_node != None:
            n_l.append(c_node.val)
            if c_node.next == None:
                break
            c_node = c_node.next
        l_idx = left - 1
        r_idx = right - 1
        #for idx, n in enumerate(n_l):
        #    if left == n:
        #        l_idx = idx
        #    elif right == n:
        #        r_idx = idx
        #if l_idx == None or r_idx == None:
        #    return head
        t_l = n_l[l_idx:r_idx+1]
        t_l.reverse()
        r_l = n_l[:l_idx] + t_l + n_l[r_idx+1:]
        r_head = ListNode()
        r_node = r_head
        r_node.val = r_l[0]
        for i in range(1,len(r_l)):
            t_node = ListNode()
            r_node.next = t_node
            r_node = r_node.next
            r_node.val = r_l[i]
        return r_head