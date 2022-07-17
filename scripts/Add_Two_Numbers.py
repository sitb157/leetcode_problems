# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list_to_int(input_list_):
    temp = [str(integer) for integer in input_list_]
    input_string_ = "".join(temp)
    output_int_ = int(input_string_)    
    return output_int_

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(l1.val)
        l1_list = [l1.val]
        l2_list = [l2.val]
        while (l1.next != None):
            l1 = l1.next
            l1_list.append(l1.val)
        
        while (l2.next != None):
            l2 = l2.next
            l2_list.append(l2.val)
        
        print(l1, l2)
        l1_list.reverse()
        l2_list.reverse()
        print(l1_list, l2_list)
        l1_int = list_to_int(l1_list)
        l2_int = list_to_int(l2_list)
        
        results = l1_int + l2_int
        results_list = list(str(results))
        results_list.reverse()
        
        l3 = ListNode(results_list[0])
        curr_node = l3
        for idx in range(1, len(results_list)):
            new_node = ListNode(results_list[idx])
            curr_node.next = new_node
            curr_node = curr_node.next
            
        print(l3)
        return l3
