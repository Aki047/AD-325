"""
Problem:
Develop a function that analyzes a patient's health record, represented as a singly linked list, and determines whether the sequence of health metrics recorded over a period exhibits a symmetrical pattern. This symmetry could indicate a return to a baseline health status or the recurrence of a condition in a cyclic manner.

Questions:
    What are the constraints on the health metric values? Specific ranges or types of values
    What is the expected length of the linked list?
    Should an empty list or a list with only one node be considered symmetric by default?
    Specific time or space complexity we need to adhere to
    Need to preserve the original linked list structure after the function execution

Process:
    create a ListNode class
    implement the isHealthRecordSymmetric function
        Find the middle of the linked list using the fast and slow pointer
        Reverse the second half of the linked list.
        Compare the first half with the reversed second half.
        Restore the list to its original state (optional but good practice).

Test Cases:
    Even symmetric list
    Not symmetric list
    Two elements symmetric
    Invalid input (not a ListNode or None)
    Non-symmetric list with repeated values

Time and Space:
Time = O(n), where n is the number of nodes in the list, each step is linear
space = O(1), extra space used does not depend on the size of the input list
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def isHealthRecordSymmetric(head: ListNode) -> bool:
    if not isinstance(head, (ListNode, type(None))):
        raise ValueError("Input must be a ListNode or None")

    if head is None or head.next is None:
        return True

    # Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    mid = slow  # Save the midpoint to restore later
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare the first and the second half
    left, right = head, prev
    is_symmetric = True
    while right:
        if left.value != right.value:
            is_symmetric = False
            break
        left = left.next
        right = right.next

    # Restore the second half of the list
    slow, prev = mid, None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    return is_symmetric

