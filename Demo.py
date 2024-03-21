"""
Assignment: Optimizing Sales Report Data By Removing Duplicate Entries

Removes duplicate entries from sales data in-place, ensuring each unique sales figure appears only once.
Maintains the original order of sales figures.

:param salesData: List of daily sales figures, sorted in non-decreasing order.
:return: Count of unique sales figures in salesData.
"""


def removeDuplicatesFromSalesData(salesData):
    if not salesData:
        print("No sales figures, try again with data")
        return 0

    uniqueIndex = 0

    for currentIndex in range(1, len(salesData)):
        if salesData[currentIndex] != salesData[uniqueIndex]:
            uniqueIndex += 1
            salesData[uniqueIndex] = salesData[currentIndex]

    return uniqueIndex +1

salesData1 = [200, 200, 300]
uniqueCount1 = removeDuplicatesFromSalesData(salesData1)
print(f"Example 1 - Unique Count: {uniqueCount1}, Modified salesData: {salesData1}")

salesData2 = [150, 150, 200, 200, 200, 250, 250, 300, 300, 350]
uniqueCount2 = removeDuplicatesFromSalesData(salesData2)
print(f"Example 2 - Unique Count: {uniqueCount2}, Modified salesData: {salesData2}")