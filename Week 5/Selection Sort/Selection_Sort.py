def selection_sort(array):
    length = len(array)

    # Outer Loop iterates through the array. In each iteration, the value of the variable i is assigned to minIndex
    for i in range(length - 1):
        min_index = i
        # Inner Loop compares the value held at the index of i. Only unsorted values are picked
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

    return array

# Test the print statement
array = [64, 25, 12, 22, 11]
print("The sorted array is: ", selection_sort(array))

def test_selection_sort():
    # Test case 1: Randomly generated array
    array1 = [64, 25, 12, 22, 11]
    assert selection_sort(array1) == [11, 12, 22, 25, 64]

    # Test case 2: Array already sorted in ascending order
    array2 = [1, 2, 3, 4, 5]
    assert selection_sort(array2) == [1, 2, 3, 4, 5]

    # Test case 3: Array sorted in descending order
    array3 = [5, 4, 3, 2, 1]
    assert selection_sort(array3) == [1, 2, 3, 4, 5]

    # Test case 4: Array with all elements being the same
    array4 = [7, 7, 7, 7, 7]
    assert selection_sort(array4) == [7, 7, 7, 7, 7]

    # Test case 5: Empty array
    array5 = []
    assert selection_sort(array5) == []

    # Test case 6: Array with one element
    array6 = [1]
    assert selection_sort(array6) == [1]

    print("All test cases pass")

test_selection_sort()
