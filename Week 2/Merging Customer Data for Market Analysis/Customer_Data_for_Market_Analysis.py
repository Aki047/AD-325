

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
