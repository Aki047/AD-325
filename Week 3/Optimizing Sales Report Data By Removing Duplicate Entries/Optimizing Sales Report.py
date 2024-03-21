"""
Removes duplicate entries from sales data in-place, ensuring each unique sales figure appears only once.
Maintains the original order of sales figures.

:param salesData: List of daily sales figures, sorted in non-decreasing order.
:return: Count of unique sales figures in salesData.
"""


def removeDuplicatesFromSalesData(salesData):
    if not salesData:
        return 0  # Return 0 if salesData is empty

    uniqueIndex = 0  # Index to place the next unique sales figure

    for currentIndex in range(1, len(salesData)):
        if salesData[currentIndex] != salesData[uniqueIndex]:
            # If the current sales figure is different from the last unique sales figure,
            # move uniqueIndex forward and update the value at uniqueIndex with the current unique sales figure.
            uniqueIndex += 1
            salesData[uniqueIndex] = salesData[currentIndex]

    # The number of unique sales figures is uniqueIndex + 1 (to account for zero indexing)
    return uniqueIndex + 1

# Example 1
salesData1 = [200, 200, 300]
uniqueCount1 = removeDuplicatesFromSalesData(salesData1)
print(f"Example 1 - Unique Count: {uniqueCount1}, Modified salesData: {salesData1}")

# Example 2
salesData2 = [150, 150, 200, 200, 200, 250, 250, 300, 300, 350]
uniqueCount2 = removeDuplicatesFromSalesData(salesData2)
print(f"Example 2 - Unique Count: {uniqueCount2}, Modified salesData: {salesData2}")
