class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


head = ListNode(2)
second = ListNode(1)
third = ListNode(5)
fourth = ListNode(3)

head.next = second
second.next = third
third.next = fourth
fourth.next = None

"""
Problem: Given the head of a singly linked list, reverse the list and return the reversed list.

Topic: Linked Lists, Pointers
Solution:
We iterate through the list and reverse the direction of each pointer using a simple iterative approach.
"""
