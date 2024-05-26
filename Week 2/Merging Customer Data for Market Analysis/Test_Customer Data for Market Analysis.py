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

    # Test case 6: Merging into a larger empty array
    customerData1 = [0, 0, 0, 0, 0, 0]
    numRecordsCustomerData1 = 0
    customerData2 = [101, 102, 103, 104, 105, 106]
    numRecordsCustomerData2 = 6
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [101, 102, 103, 104, 105, 106]

    # Test case 7: Merging with one element larger than all in the other array
    customerData1 = [1, 3, 5, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [6, 7, 8]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [1, 3, 5, 6, 7, 8]

    # Test case 8: Merging with negative numbers
    customerData1 = [-3, -1, 2, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [-2, 0, 1]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [-3, -2, -1, 0, 1, 2]

    # Test case 9: Merging with one array completely greater than the other
    customerData1 = [1, 2, 3, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [4, 5, 6]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [1, 2, 3, 4, 5, 6]

    # Test case 10: Both arrays contain the same elements
    customerData1 = [1, 1, 1, 0, 0, 0]
    numRecordsCustomerData1 = 3
    customerData2 = [1, 1, 1]
    numRecordsCustomerData2 = 3
    merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
    assert customerData1 == [1, 1, 1, 1, 1, 1]

    print("All test cases passed!")

# Run the test cases
test_merge_customer_data()
