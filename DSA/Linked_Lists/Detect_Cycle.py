class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second

print(has_cycle(head))

"""
Given the head of a singly linked list, return True if there is a cycle in the linked list. Otherwise, return False.

Approach:
Use two pointers, slow and fast.
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
If there is a cycle, the fast pointer will eventually meet the slow pointer.
If the fast pointer reaches the end (None), then there is no cycle.
"""
