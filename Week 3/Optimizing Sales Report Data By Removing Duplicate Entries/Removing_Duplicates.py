"""
Problem: Removes duplicate entries from sales data in-place, ensuring each unique sales figure appears only once.
Maintains the original order of sales figures.
List of daily sales figures, sorted in non-decreasing order.
return the Count of unique sales figures in salesData.

Process:
define variable
Check if list is empty, if yes return 0
Start loop, index 1, to end of the list
compare current element with uniqueindex
If different, increment uniqueIndex and update salesData[uniqueIndex] with salesData[currentIndex].
after loop ends # unique sales figures is uniqueIndex +1

Questions:
How does it handle duplicates
empty lists?
Single element?

Time and Space Complexity:
O(n), single loop that iterates through list once
O(1), modifies list in place, and uses a constant amount of extra space
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

"""
Test case 1: Basic case with duplicates.
Test case 2: List with multiple duplicates.
Test case 3: List with no duplicates.
Test case 4: List where all elements are duplicates.
Test case 5: Empty list.
Test case 6: List with a single element.
Test case 7: Large list with various duplicates.
Test case 8: List with alternating duplicates.
Test case 9: Increasing sequence with some duplicates.
Test case 10: List with all identical elements.

"""