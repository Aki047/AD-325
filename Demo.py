"""
Merging Customer Data for Market Analysis

 Goal: write a program that merges two sets of customer data, each sorted by customer ID, into a single, combined dataset also sorted by customer ID.

Question:
Do we need to handle duplicate IDs uniquely, or should they be merged as is

Are we considering any specific data fields beyond customer IDs, or is this merge solely based on IDs

Can we assume the input arrays are always correctly sorted, or should our solution include a validation check

Approach:
a two-pointer technique to merge the arrays in place, minimizing space usage
"""

def merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2):
    ptrCustomerData1, ptrCustomerData2 = numRecordsCustomerData1 - 1, numRecordsCustomerData2 - 1

    for i in range(numRecordsCustomerData1 + numRecordsCustomerData2 - 1, -1, -1):
        if ptrCustomerData2 < 0:
            break
        if ptrCustomerData1 >= 0 and customerData1[ptrCustomerData1] > customerData2[ptrCustomerData2]:
            customerData1[i] = customerData1[ptrCustomerData1]
            ptrCustomerData1 -= 1
        else:
            customerData1[i] = customerData2[ptrCustomerData2]
            ptrCustomerData2 -= 1

customerData1 = [101, 104, 107, 0, 0, 0]
numRecordsCustomerData1 = 3
customerData2 = [102, 105, 108]
numRecordsCustomerData2 = 3
merge_customer_data(customerData1, numRecordsCustomerData1, customerData2, numRecordsCustomerData2)
print(customerData1)