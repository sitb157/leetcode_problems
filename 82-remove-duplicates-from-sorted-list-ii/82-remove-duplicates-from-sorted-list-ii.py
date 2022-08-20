# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t_node = head
        t_l = []
        while t_node != None:
            t_l.append(t_node.val)
            if t_node.next == None:
                break
            t_node = t_node.next
                
        r_l = []
        if len(t_l) == 0:
            return None
        elif len(t_l) == 1:
            r_l = t_l
        else:
            for i in range(len(t_l)):
                if i == 0:
                    if t_l[i] == t_l[i+1]:
                        continue
                elif i == (len(t_l) - 1):
                    if t_l[i-1] == t_l[i]:
                        continue
                else:
                    if (t_l[i-1] == t_l[i]) or (t_l[i] == t_l[i+1]):
                        continue
                r_l.append(t_l[i])
        if len(r_l) == 0:
            return None
        print(r_l)
        r_head = ListNode()
        r_head.val = r_l[0]
        c_node = r_head
        for r in r_l[1:]:
            t_node = ListNode()
            c_node.next = t_node
            c_node = c_node.next
            c_node.val = r
        return r_head
    