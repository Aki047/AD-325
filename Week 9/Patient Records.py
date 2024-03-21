""""
Problem Statement: Patient Records

integrate both sets of records into a single, sorted list, merge records without losing any information and maintaining the sort order based on SSN.

Time Complexity: O(n + m)
Space Complexity: O(1)

Q's 

How to handle same SSN/patient on both sets of records?
How is patent data recorded on each node


Process: 

Linked through nodes, compare SSN of head nodes and append to nodes of smaller ones. Continue till finished

"""""
class ListNode:
    def __init__(self, ssn, name, age, next=None):
        # Initialize each node with patient's SSN, name, age, and a pointer to the next node
        self.ssn = ssn
        self.name = name
        self.age = age
        self.next = next

    def __repr__(self):
        # Helper method to print out the node's details
        return f"{self.ssn}: {self.name}, {self.age} years"

def merge_sorted_lists(HealthMerge, CarePlus):
    # Validation checks for empty lists
    if not HealthMerge:
        print('No Patient Records Found, Update HealthMerge records')
        return CarePlus  # If HealthMerge list is empty, return CarePlus list as is
    if not CarePlus:
        print('No Patient Records Found, Update CarePlus records')
        return HealthMerge  # If CarePlus list is empty, return HealthMerge list as is

    # Create a dummy node as the starting point of the merged list
    dummy = ListNode(0, "", 0)
    tail = dummy  # Tail helps in appending nodes to the merged list

    # Iterate through both lists until one is done
    while HealthMerge and CarePlus:
        # Compare SSN of current nodes in both lists to determine which to append to the merged list
        if HealthMerge.ssn <= CarePlus.ssn:
            tail.next = HealthMerge  # Append HealthMerge node to merged list
            HealthMerge = HealthMerge.next  # Move to the next node in HealthMerge
        else:
            tail.next = CarePlus  # Append CarePlus node to merged list
            CarePlus = CarePlus.next  # Move to the next node in CarePlus
        tail = tail.next  # Move the tail pointer forward

    # After the loop, at least one list is exhausted. Append the remainder of the non-empty list to merged list
    tail.next = HealthMerge if HealthMerge else CarePlus

    return dummy.next  # Return the head of the merged list, which follows the dummy node

def print_linked_list(head):
    """Prints the contents of a linked list starting from the head node."""
    current = head
    while current:
        print(current)
        current = current.next

# Creating test patient records for HealthMerge
patient1 = ListNode(123456789, "John Doe", 30)
patient2 = ListNode(223456789, "Jane Smith", 25)
# Linking patient records to form the HealthMerge list
patient1.next = patient2
HealthMerge_head = patient1

# Creating test patient records for CarePlus
patient3 = ListNode(123456789, "John Doe", 30)  # Duplicate SSN as an example
patient4 = ListNode(323456789, "Alice Johnson", 28)
# Linking patient records to form the CarePlus list
patient3.next = patient4
CarePlus_head = patient3

# Merging the HealthMerge and CarePlus lists
merged_list_head = merge_sorted_lists(HealthMerge_head, CarePlus_head)

# Printing the merged list
print("Merged Patient Records:")
print_linked_list(merged_list_head)