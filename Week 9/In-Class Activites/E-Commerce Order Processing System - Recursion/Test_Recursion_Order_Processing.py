import unittest
from Recursion_Order_Processing import Order, Order_Queue


class TestOrderQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Order_Queue()

    # Test 1: Adding orders to the list
    def test_add_orders(self):
        order1 = Order(1, "Alice", "Laptop", "2023-05-01", "10:00 AM")
        order2 = Order(2, "Bob", "Phone", "2023-05-02", "11:00 AM")
        order3 = Order(3, "Charlie", "Tablet", "2023-05-03", "12:00 PM")
        self.queue.append(order1)
        self.queue.append(order2)
        self.queue.append(order3)

        self.assertEqual(self.queue.Packing_List(), [str(order1), str(order2), str(order3)],
                         "Test failed: Orders should be added in the correct order.")

    # Test 2: Displaying orders in the order they were added
    def test_display_orders(self):
        order1 = Order(1, "Alice", "Laptop", "2023-05-01", "10:00 AM")
        order2 = Order(2, "Bob", "Phone", "2023-05-02", "11:00 AM")
        self.queue.append(order1)
        self.queue.append(order2)

        self.assertEqual(self.queue.Packing_List(), [str(order1), str(order2)],
                         "Test failed: Orders should be displayed in the order they were added.")

    # Test 3: Reversing the list of multiple orders
    def test_reverse_orders(self):
        order1 = Order(1, "Alice", "Laptop", "2023-05-01", "10:00 AM")
        order2 = Order(2, "Bob", "Phone", "2023-05-02", "11:00 AM")
        order3 = Order(3, "Charlie", "Tablet", "2023-05-03", "12:00 PM")
        self.queue.append(order1)
        self.queue.append(order2)
        self.queue.append(order3)

        self.queue.reverse_recursive()
        self.assertEqual(self.queue.Packing_List(), [str(order3), str(order2), str(order1)],
                         "Test failed: Orders should be reversed correctly.")

    # Test 4: Reversing a single order
    def test_reverse_single_order(self):
        order1 = Order(1, "Alice", "Laptop", "2023-05-01", "10:00 AM")
        self.queue.append(order1)

        self.queue.reverse_recursive()
        self.assertEqual(self.queue.Packing_List(), [str(order1)],
                         "Test failed: Single order should remain the same after reverse.")

    # Test 5: Reversing an empty list
    def test_reverse_empty_list(self):
        self.queue.reverse_recursive()
        self.assertEqual(self.queue.Packing_List(), "The order queue is empty.",
                         "Test failed: Empty list should remain empty after reverse.")


if __name__ == "__main__":
    unittest.main()
