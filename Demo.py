"""
Purpose:
Ordering system for e-commerce where orders are processed sequentially, oldest to newest
reverse the ordering system so newest is processed first, done with Singly Linked List

Questions:
Size of order list?
The format for the order:
    orderID, Customer details, order details, order date and order time
What if Order_Que is empty? Should it check and break?
How to handle Duplicate orders?
What if an order attribute is missiing?
Check & display message with order details
What if orders are submitted at same day and time how to sort
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
    Adding orders to the linked list.
    Displaying the list of orders in the order they were added.
    Reversing the linked list.
    Displaying the list of orders after reversal to ensure the most recent order is processed first
Edge Cases:
    Empty Order Queue
    Single Order
    Duplicate Order
    Missing Attributes

Time and Space Complexity:
Time: O(n), n is the number of orders
Space:O(1), Order Storage

"""

class Order:
    def __init__(self, order_id, customer_details, order_details, order_date, order_time):
        self.order_id = order_id
        self.customer_details = customer_details
        self.order_details = order_details
        self.order_date = order_date
        self.order_time = order_time
        self.next = None  # Points to the next order in the list

    def __str__(self):
        return (f"Order ID: {self.order_id}, Customer: {self.customer_details}, "
                f"Order Details: {self.order_details}, Order Date: {self.order_date}, "
                f"Order Time: {self.order_time}")

    def get_datetime(self):
        return datetime.strptime(f"{self.order_date} {self.order_time}", "%Y-%m-%d %I:%M %p")

class Order_Queue:
# define class attributes, start empty que
def __init__(self):
    self.head = None

#append method
    def append(self, order):
        # if the list is empty place at position 1 if not
        if self.head is None or order.get_datetime() < self.head.get_datetime():
            order.next = self.head
            self.head = order

        else:
            # transverse list, find position
            current = self.head
            while current.next is not None and current.next.get_datetime() <= order.get_datetime():
                current = current.next
            order.next = current.next
            current.next = order

    # Packing list
    def Packing_List(self):
        orders = []
        current = self.head
        while current is not None:
            orders.append(str(current))
            current = current.next

            print(orders)
        return orders

# Reverse the linked list so that the last order becomes the first and vice versa.
   def reverse(self):
       if self.head is None:
           print("The order queue is empty. No need to reverse.")
           return

       prev = None
       current = self.head
       while current is not None:
           next_node = current.next
           current.next = prev
           prev = current
           current = next_node
       self.head = prev







