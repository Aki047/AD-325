from datetime import datetime

class Order:
    def __init__(self, order_id, customer_details, order_details, order_date, order_time):
        self.order_id = order_id
        self.customer_details = customer_details
        self.order_details = order_details
        self.order_date = order_date
        self.order_time = order_time
        self.next = None  # Points to the next order in the list

    def __str__(self):
        # Return a string representation of the Order object.
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
        # Create a list of orders from the first to the last.
        orders = []
        current = self.head
        while current is not None:
            orders.append(str(current))
            current = current.next
        return orders

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Temporarily store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev and current one step forward
            current = next_node
        self.head = prev  # Reset the head to the new first node

# Example script to test the functionality
if __name__ == '__main__':
    # Initialize order queue
    order_queue = Order_Queue()

    # Append orders
    orders = [
        Order(order_id=1, customer_details="Alice", order_details="Laptop", order_date="2024-05-25", order_time="10:00 AM"),
        Order(order_id=2, customer_details="Bob", order_details="Phone", order_date="2024-05-26", order_time="11:00 AM"),
        Order(order_id=3, customer_details="Charlie", order_details="Tablet", order_date="2024-05-27", order_time="12:00 PM")
    ]
    for order in orders:
        order_queue.append(order)

    # Print original packing list
    print("Original Packing List:")
    for order in order_queue.Packing_List():
        print(order)

    # Reverse the order queue
    order_queue.reverse()

    # Print reversed packing list
    print("\nReversed Packing List:")
    for order in order_queue.Packing_List():
        print(order)
