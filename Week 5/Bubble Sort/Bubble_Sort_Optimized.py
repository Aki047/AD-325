def Bubble_Sort(array):
    length = len(array)
    for pass_num in range(length):
        swapped = False  # Initialize the swapped flag to detect any swaps during this pass
        for current_index in range(0, length - pass_num - 1):
            if array[current_index] > array[current_index + 1]:
                # Swap if the current element is greater than the next element
                array[current_index], array[current_index + 1] = array[current_index + 1], array[current_index]
                swapped = True  # Set the swapped flag to True if a swap is made
        if not swapped:
            # If no swaps were made during this pass, the array is already sorted, early termination
            break
    return array

# Test cases for Optimized Bubble Sort
def test_Bubble_Sort():
    # Randomly generated array of integers
    assert Bubble_Sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    # Already sorted array
    assert Bubble_Sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Array sorted in descending order
    assert Bubble_Sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Array with all identical elements
    assert Bubble_Sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    # Edge case: empty array
    assert Bubble_Sort([]) == []
    # Edge case: single-element array
    assert Bubble_Sort([1]) == [1]

    print("All test cases passed!")


# Run tests
test_Bubble_Sort()