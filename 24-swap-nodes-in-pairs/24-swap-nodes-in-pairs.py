# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        current_node = head
        n_l = [current_node.val]
        while current_node.next != None:
            current_node = current_node.next    
            n_l.append(current_node.val)
        
        l_l = len(n_l)
        print(n_l)
        i = 0
        if l_l == 0:
            return ListNode().next
        elif l_l == 1:
            result_head = ListNode(n_l[0])
            return result_head
        else:
            i += 2
            result_head = ListNode(n_l[i-1])
            current_r_node = result_head
            new_node = ListNode(n_l[i-2])
            current_r_node.next = new_node
            current_r_node = current_r_node.next
        while i <= (l_l-2):
            i += 2
            new_node = ListNode(n_l[i-1])
            current_r_node.next = new_node
            current_r_node = current_r_node.next
            new_node = ListNode(n_l[i-2])
            current_r_node.next = new_node
            current_r_node = current_r_node.next
        if (l_l - i) == 1:
            new_node = ListNode(n_l[-1])
            current_r_node.next = new_node
            current_r_node = current_r_node.next
        return result_head
