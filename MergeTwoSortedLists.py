"""
You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should
be made by splicing together the nodes of the first two lists. Return the head of the merged linked list. 
Ex: 
Input: list1 = [1, 2, 4], list2 = [1, 3, 4] 
Output: [1, 1, 2, 3, 4, 4]
"""

from SLL import *

def mergeTwoLists(list1, list2):
    dummy = Node(-1)
    p1 = list1
    p2 = list2

    while p1 and p2:
        if p1.data <= p2.data:
            dummy.next = p1
            p1 = p1.next
        else:
            dummy.next = p2
            p2 = p2.next
        dummy = dummy.next

    if p1 is not None:
        dummy.next = p1
    else:
        dummy.next = p2

    return dummy.next

list1 = SinglyLinkedList()
list2 = SinglyLinkedList()
list1.create_linked_list([1, 2, 4])
list2.create_linked_list([1, 3, 4])
list1.print_linked_list()
list2.print_linked_list()

mergeTwoLists(list1.head, list2.head)

list1.print_linked_list()