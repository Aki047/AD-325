'''
Process:
define function
2 pointer initilized, point to last element in customerData1 & customerData2
use loop to fill customerData1 from end to beginning
compare the elements indicated by the pointers and place the larger element at the current position in customerData1
repeat until all elements are merged

Questions:
How does it handle duplicates
what validation checks should it perform
max array or time compelxity requirments
Error Handling:
    if one list is <0 then break
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
Time Complexity
o(n+m) customerData1 = n, and customerData2 =m

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

