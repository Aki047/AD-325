from Customer_Data_for_Market_Analysis import merge_customer_data

def test_merge_customer_data():
    # Test case 1: Both arrays are empty
    customerData1 = []
    numRecordsCustomerData1 = 0
    customerData2 = []
    numRecordsCustomerData2 = 0
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == []

    # Test case 2: One array is empty
    customerData1 = [101, 104, 107, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = []
    numRecordsCustomerData2 = 0
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [101, 104, 107, 0, 0, 0]

    # Test case 3: Both arrays have one element
    customerData1 = [103, 0]
    numRecordsCustomerData1 = 1
    customerData2 = [102]
    numRecordsCustomerData2 = 1
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [102, 103]

    # Test case 4: Arrays with multiple elements
    customerData1 = [101, 104, 107, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [102, 105, 108]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [101, 102, 104, 105, 107, 108]

    # Test case 5: Arrays with duplicate elements
    customerData1 = [101, 102, 104, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [102, 105, 107]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [101, 102, 102, 104, 105, 107]

    print("All test cases passed!")

# Run the test cases
test_merge_customer_data()
