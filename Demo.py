"""
Problem:
ou need to process the most recent orders first to ensure faster delivery for last-minute purchases. The orders are currently stored in a singly linked list, with the head being the first order received. Your task is to reverse the list so the most recent orders are processed first. Reverse the list using a reverse function that modifies the links between nodes in the list to invert the order of the nodes. After reversal, the display() function should present the orders starting from the most recently added.

Questions:
How to handle empty attributes
    recursive reversal of the linked list, are there any constraints on the maximum depth of recursion we need to be aware of
    After reversing the list, how should we confirm the operation was successful?
    edge cases like an empty list, a list with one order, and a list with multiple orders?
Process:
    Create Class Order: ID, Customer name, details, date, time
    Return a string representation of the Order object.
    Combine order_date and order_time into a datetime object for comparison
    Initialize an empty Order_Queue.
    Append a new order to the end of the list, if empty, set the new order as the head, sort by date and time
        Traverse the list to find the correct position for the new order
    Print out the list of orders from the first to the last.
    Reverse the linked list so that the last order becomes the first and vice versa.

Test Cases:
Empty list
single element list
multi element list
orders at different times

Edge Cases:


Time and Space Complexity:
Time = O(n) for the sequence of operations.
space = O(n) due to the recursion call stack and the temporary storage used

"""
class Order:
    def __init__(self, order_id, customer_details, order_details, order_date, order_time):
        # Checks if all attributes are provided
        if not all([order_id, customer_details, order_details, order_date, order_time]):
            raise ValueError("All order attributes must be provided.")

        self.order_id = order_id
        self.customer_details = customer_details
        self.order_details = order_details
        self.order_date = order_date
        self.order_time = order_time
        self.next = None  # Points to the next order

    def __str__(self):
        return (f"Order ID: {self.order_id}, Customer: {self.customer_details}, "
                f"Order Details: {self.order_details}, Order Date: {self.order_date}, "
                f"Order Time: {self.order_time}")

    def get_datetime(self):
        # Combine order_date and order_time into a datetime object for comparison
        return datetime.strptime(f"{self.order_date} {self.order_time}", "%Y-%m-%d %I:%M %p")

class Order_Queue:
    def __init__(self):
        # Initialize an empty Order_Queue.
        self.head = None  # Head of the list, initially set to None
    def append(self, order):
        # Append a new order to the list in sorted order.
        if self.head is None or order.get_datetime() < self.head.get_datetime():
            # If the list is empty or the new order is older than the head, insert at the head
            order.next = self.head
            self.head = order
        else:
            # Traverse the list to find the correct position for the new order
            current = self.head
            while current.next is not None and current.next.get_datetime() <= order.get_datetime():
                current = current.next
            order.next = current.next
            current.next = order

    def Packing_List(self):
        # Check if queue is empty, display message if true
        if self.head is None:
            return "The order queue is empty."

        # Print out the list of orders from the first to the last.
        orders = []
        current = self.head
        while current is not None:
            orders.append(str(current))
            current = current.next
        return orders

    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)
        self.head = _reverse_recursive(self.head, None)
