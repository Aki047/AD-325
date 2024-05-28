def insertion_sort(array):
    # Iterate over the array starting from the second element
    for index in range(1, len(array)):
        # Store the value of the current element
        current_value = array[index]
        # Initialize the position to place the current element
        position = index

        # Shift elements of the sorted section to the right to make space for the current element
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1

        # Place the current element in its correct position
        array[position] = current_value

    return array


def test_insertion_sort():
    # Test 1: Randomly generated array of integers
    assert insertion_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    # Test 2: Already sorted array
    assert insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Test 3: Array sorted in descending order
    assert insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Test 4: Array with all identical elements
    assert insertion_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    # Test 5: Edge case - empty array
    assert insertion_sort([]) == []
    # Test 6: Edge case - single-element array
    assert insertion_sort([1]) == [1]
    # Test 7: Nearly sorted array
    assert insertion_sort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
    # Test 8: Large array in reverse order
    assert insertion_sort([i for i in range(1000, 0, -1)]) == [i for i in range(1, 1001)]
    # Test 9: Small array
    assert insertion_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    # Test 10: Array with negative numbers
    assert insertion_sort([0, -1, 3, -10, 5, 2, -3]) == [-10, -3, -1, 0, 2, 3, 5]
    # Test 11: Stability test with tuples
    original_tuples = [(3, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    sorted_tuples = insertion_sort(original_tuples.copy())
    assert sorted_tuples == [(1, 'b'), (2, 'c'), (3, 'a'), (3, 'd')]

    # Displaying original and sorted tuples to demonstrate stability
    print("Original tuples:", original_tuples)
    print("Sorted tuples:", sorted_tuples)

    print("All test cases passed!")


if __name__ == "__main__":
    test_insertion_sort()