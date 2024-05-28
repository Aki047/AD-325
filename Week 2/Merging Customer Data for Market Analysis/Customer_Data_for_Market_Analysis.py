'''
Purpose:

Process:
define function with 4 parameters:
    customerData1: A list containing customer data, with extra space at the end to accommodate data from customerData2.
    numRecordsCustomerData1: The number of valid records initially present in customerData1.
    customerData2: A list containing customer data to be merged into customerData1.
    numRecordsCustomerData2: The number of valid records in customerData2.

Initialize pointers to the last valid elements of both arrays
#Start merging from the end of both arrays

Questions:

Error Handling:


Test Cases:
    # Test case 1: Both arrays are empty
    # Test case 2: One array is empty
    # Test case 3: Both arrays have one element
    # Test case 4: Arrays with multiple elements
    # Test case 5: Arrays with duplicate elements
    # Test case 6: Merging into a larger empty array
    # Test case 7: Merging with one element larger than all in the other array
    # Test case 8: Merging with negative numbers
    # Test case 9: Merging with one array completely greater than the other
    # Test case 10: Both arrays contain the same elements

'''

def merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2):
    # Initialize pointers to the last valid elements of both arrays
    ptrCustomerData1, ptrCustomerData2 = numRecordsCustomerData1 - 1, numRecordsCustomerData2 - 1

    # Start merging from the end of both arrays
    for i in range(numRecordsCustomerData1 + numRecordsCustomerData2 - 1, -1, -1):
        if ptrCustomerData2 < 0:
            break
        if ptrCustomerData1 >= 0 and customerData1[ptrCustomerData1] > customerData2[ptrCustomerData2]:
            customerData1[i] = customerData1[ptrCustomerData1]
            ptrCustomerData1 -= 1
        else:
            customerData1[i] = customerData2[ptrCustomerData2]
            ptrCustomerData2 -= 1

    # No need to return, customerData1 is modified in-place


# Example usage:
customerData1 = [101, 104, 107, 0, 0, 0]
numRecordsCustomerData1 = 3
customerData2 = [102, 105, 108]
numRecordsCustomerData2 = 3
merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
print(customerData1)  # Output: [101, 102, 104, 105, 107, 108]

