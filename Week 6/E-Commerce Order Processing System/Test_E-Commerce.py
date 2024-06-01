import unittest
from E_Commerce_Order_Processing import Order, Order_Queue

class TestOrderQueue(unittest.TestCase):

    # Test 1: Tests behavior with an empty order queue
    def test_empty_order_queue(self):
        print("\nTesting Empty Order Queue")
        empty_list = Order_Queue()
        self.assertEqual(empty_list.Packing_List(), "The order queue is empty.")

        empty_list.reverse()
        self.assertEqual(empty_list.Packing_List(), "The order queue is empty.")

    # Test 2: Tests behavior with a single order in the queue
    def test_single_order(self):
        print("\nTesting Single Order in Queue")
        single_order_list = Order_Queue()
        single_order = Order(order_id=4, customer_details="Bob Brown", order_details="Monitor", order_date="2024-05-25",
                             order_time="12:00 PM")
        single_order_list.append(single_order)
        expected_output = [
            "Order ID: 4, Customer: Bob Brown, Order Details: Monitor, Order Date: 2024-05-25, Order Time: 12:00 PM"
        ]
        self.assertEqual(single_order_list.Packing_List(), expected_output)

        single_order_list.reverse()
        self.assertEqual(single_order_list.Packing_List(), expected_output)

    # Test 3: Tests behavior with duplicate orders
    def test_duplicate_orders(self):
        print("\nTesting Duplicate Orders")
        duplicate_order1 = Order(order_id=5, customer_details="Charlie Black", order_details="Keyboard",
                                 order_date="2024-05-25", order_time="01:00 PM")
        duplicate_order2 = Order(order_id=5, customer_details="Charlie Black", order_details="Keyboard",
                                 order_date="2024-05-25", order_time="01:00 PM")
        duplicate_order_list = Order_Queue()
        duplicate_order_list.append(duplicate_order1)
        duplicate_order_list.append(duplicate_order2)
        expected_output = [
            "Order ID: 5, Customer: Charlie Black, Order Details: Keyboard, Order Date: 2024-05-25, Order Time: 01:00 PM",
            "Order ID: 5, Customer: Charlie Black, Order Details: Keyboard, Order Date: 2024-05-25, Order Time: 01:00 PM"
        ]
        self.assertEqual(duplicate_order_list.Packing_List(), expected_output)

        duplicate_order_list.reverse()
        self.assertEqual(duplicate_order_list.Packing_List(), list(reversed(expected_output)))

    # Test 4: Tests behavior when an order is missing mandatory attributes
    def test_missing_attributes(self):
        print("\nTesting Missing Attributes")
        with self.assertRaises(ValueError):
            Order(order_id=6, customer_details="", order_details="Mouse", order_date="2024-05-24",
                  order_time="02:00 PM")

    # Test 5: Orders submitted at the same date and time are appended correctly
    def test_orders_with_same_date_time(self):
        print("\nTesting Orders with Same Date and Time")
        same_time_order1 = Order(order_id=7, customer_details="Dana White", order_details="Webcam",
                                 order_date="2024-05-23", order_time="03:00 PM")
        same_time_order2 = Order(order_id=8, customer_details="Eve Green", order_details="Headset",
                                 order_date="2024-05-23", order_time="03:00 PM")
        same_time_order_list = Order_Queue()
        same_time_order_list.append(same_time_order1)
        same_time_order_list.append(same_time_order2)
        expected_output = [
            "Order ID: 7, Customer: Dana White, Order Details: Webcam, Order Date: 2024-05-23, Order Time: 03:00 PM",
            "Order ID: 8, Customer: Eve Green, Order Details: Headset, Order Date: 2024-05-23, Order Time: 03:00 PM"
        ]
        self.assertEqual(same_time_order_list.Packing_List(), expected_output)

    # Test 6: Tests behavior when an order has invalid attributes
    def test_order_attribute_validation(self):
        print("\nTesting Order Attribute Validation")
        with self.assertRaises(ValueError):
            Order(order_id=9, customer_details=None, order_details="Chair", order_date="2024-05-22",
                  order_time="04:00 PM")

    # Test 7: Appending multiple orders and checking order
    def test_multiple_orders(self):
        print("\nTesting Multiple Orders")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:00 AM"),
            Order(order_id=3, customer_details="Customer C", order_details="Item 3", order_date="2024-05-27",
                  order_time="12:00 PM")
        ]
        for order in orders:
            order_queue.append(order)
        expected_output = [
            "Order ID: 1, Customer: Customer A, Order Details: Item 1, Order Date: 2024-05-25, Order Time: 10:00 AM",
            "Order ID: 2, Customer: Customer B, Order Details: Item 2, Order Date: 2024-05-26, Order Time: 11:00 AM",
            "Order ID: 3, Customer: Customer C, Order Details: Item 3, Order Date: 2024-05-27, Order Time: 12:00 PM"
        ]
        self.assertEqual(order_queue.Packing_List(), expected_output)

    # Test 8: Reversing a list with an even number of orders
    def test_reverse_even_orders(self):
        print("\nTesting Reverse with Even Number of Orders")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:00 AM")
        ]
        for order in orders:
            order_queue.append(order)
        order_queue.reverse()
        expected_output = [
            "Order ID: 2, Customer: Customer B, Order Details: Item 2, Order Date: 2024-05-26, Order Time: 11:00 AM",
            "Order ID: 1, Customer: Customer A, Order Details: Item 1, Order Date: 2024-05-25, Order Time: 10:00 AM"
        ]
        self.assertEqual(order_queue.Packing_List(), expected_output)

    # Test 9: Reversing a list with an odd number of orders
    def test_reverse_odd_orders(self):
        print("\nTesting Reverse with Odd Number of Orders")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:00 AM"),
            Order(order_id=3, customer_details="Customer C", order_details="Item 3", order_date="2024-05-27",
                  order_time="12:00 PM")
        ]
        for order in orders:
            order_queue.append(order)
        order_queue.reverse()
        expected_output = [
            "Order ID: 3, Customer: Customer C, Order Details: Item 3, Order Date: 2024-05-27, Order Time: 12:00 PM",
            "Order ID: 2, Customer: Customer B, Order Details: Item 2, Order Date: 2024-05-26, Order Time: 11:00 AM",
            "Order ID: 1, Customer: Customer A, Order Details: Item 1, Order Date: 2024-05-25, Order Time: 10:00 AM"
        ]
        self.assertEqual(order_queue.Packing_List(), expected_output)

    # Test 11: Checking order after multiple reversals
    def test_multiple_reversals(self):
        print("\nTesting Multiple Reversals")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:00 AM")
        ]
        for order in orders:
            order_queue.append(order)
        order_queue.reverse()
        order_queue.reverse()
        expected_output = [
            "Order ID: 1, Customer: Customer A, Order Details: Item 1, Order Date: 2024-05-25, Order Time: 10:00 AM",
            "Order ID: 2, Customer: Customer B, Order Details: Item 2, Order Date: 2024-05-26, Order Time: 11:00 AM"
        ]
        self.assertEqual(order_queue.Packing_List(), expected_output)

    # Test 12: Appending orders with mixed date and time formats
    def test_mixed_date_time_formats(self):
        print("\nTesting Mixed Date and Time Formats")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-02-29",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:59 PM")
        ]
        for order in orders:
            order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertEqual(len(output), 2)

    # Test 13: Handling orders with long customer details
    def test_long_customer_details(self):
        print("\nTesting Long Customer Details")
        order_queue = Order_Queue()
        long_name = "A" * 1000
        order = Order(order_id=1, customer_details=long_name, order_details="Item 1", order_date="2024-05-25",
                      order_time="10:00 AM")
        order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertIn(long_name, output[0])

    # Test 14: Handling orders with long order details
    def test_long_order_details(self):
        print("\nTesting Long Order Details")
        order_queue = Order_Queue()
        long_details = "B" * 1000
        order = Order(order_id=1, customer_details="Customer A", order_details=long_details, order_date="2024-05-25",
                      order_time="10:00 AM")
        order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertIn(long_details, output[0])

    # Test 15: Checking duplicate order IDs
    def test_duplicate_order_ids(self):
        print("\nTesting Duplicate Order IDs")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=1, customer_details="Customer B", order_details="Item 2", order_date="2024-05-26",
                  order_time="11:00 AM")
        ]
        for order in orders:
            order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertEqual(len(output), 2)

    # Test 16: Handling empty strings in order details
    def test_empty_strings_in_attributes(self):
        print("\nTesting Empty Strings in Attributes")
        with self.assertRaises(ValueError):
            Order(order_id=1, customer_details="Customer A", order_details="", order_date="2024-05-25",
                  order_time="10:00 AM")

    # Test 17: Handling leap year dates
    def test_edge_case_dates(self):
        print("\nTesting Edge Case Dates")
        order_queue = Order_Queue()
        order = Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-02-29",
                      order_time="10:00 AM")
        order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertIn("2024-02-29", output[0])

    # Test 18: Checking correct insertion order for consecutive orders
    def test_consecutive_orders(self):
        print("\nTesting Consecutive Orders")
        order_queue = Order_Queue()
        orders = [
            Order(order_id=1, customer_details="Customer A", order_details="Item 1", order_date="2024-05-25",
                  order_time="10:00 AM"),
            Order(order_id=2, customer_details="Customer B", order_details="Item 2", order_date="2024-05-25",
                  order_time="10:01 AM")
        ]
        for order in orders:
            order_queue.append(order)
        output = order_queue.Packing_List()
        self.assertIn("Order ID: 1", output[0])
        self.assertIn("Order ID: 2", output[1])

    # Test 19: Handling empty strings in order id
    def test_empty_order_id(self):
        print("\nTesting Empty Order ID")
        with self.assertRaises(ValueError):
            Order(order_id="", customer_details="Harley Quinn", order_details="Phone", order_date="2024-05-25",
                  order_time="10:00 AM")

    # Test 20: Handling empty strings in customer details
    def test_empty_customer_details(self):
        print("\nTesting Empty Customer Details")
        with self.assertRaises(ValueError):
            Order(order_id=1, customer_details="", order_details="Phone", order_date="2024-05-25",
                  order_time="10:00 AM")

    # Test 21: Handling None as an order (should raise error)
    def test_none_order(self):
        print("\nTesting None as an Order")
        order_queue = Order_Queue()
        with self.assertRaises(AttributeError):
            order_queue.append(None)

    # Test 22: Tests verifying the reversal of the orders
    def test_reverse_orders_with_same_date_time(self):
        print("\nTesting Reverse Orders with Same Date and Time")
        same_time_order1 = Order(order_id=7, customer_details="Dana White", order_details="Webcam",
                                 order_date="2024-05-23", order_time="03:00 PM")
        same_time_order2 = Order(order_id=8, customer_details="Eve Green", order_details="Headset",
                                 order_date="2024-05-23", order_time="03:00 PM")
        same_time_order_list = Order_Queue()
        same_time_order_list.append(same_time_order1)
        same_time_order_list.append(same_time_order2)
        same_time_order_list.reverse()
        expected_output = [
            "Order ID: 8, Customer: Eve Green, Order Details: Headset, Order Date: 2024-05-23, Order Time: 03:00 PM",
            "Order ID: 7, Customer: Dana White, Order Details: Webcam, Order Date: 2024-05-23, Order Time: 03:00 PM"
        ]
        self.assertEqual(same_time_order_list.Packing_List(), expected_output)

if __name__ == '__main__':
    unittest.main()
