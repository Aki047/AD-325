def selection_sort_descending(array):
    length = len(array)

    for i in range(length - 1):
        max_index = i
        for j in range(i + 1, length):
            # Change the comparison operator in inner loop to sort in descending order
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

    return array


# Test the print statement
test_array = [64, 25, 12, 22, 11]
print("The sorted array in descending order is: ", selection_sort_descending(test_array))


def stable_selection_sort(array):
    length = len(array)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        # Instead of swapping, shift the elements
        min_value = array[min_index]
        while min_index > i:
            array[min_index] = array[min_index - 1]
            min_index -= 1
        array[i] = min_value

    return array


# Test print statement
test_array = [64, 25, 12, 22, 11]
print("The stable sorted array is: ", stable_selection_sort(test_array))


def test_selection_sort_descending():
    # Test case 1: Randomly generated array
    array1 = [64, 25, 12, 22, 11]
    assert selection_sort_descending(array1) == [64, 25, 22, 12, 11]

    # Test case 2: Array already sorted in descending order
    array2 = [5, 4, 3, 2, 1]
    assert selection_sort_descending(array2) == [5, 4, 3, 2, 1]

    # Test case 3: Array sorted in ascending order
    array3 = [1, 2, 3, 4, 5]
    assert selection_sort_descending(array3) == [5, 4, 3, 2, 1]

    # Test case 4: Array with all elements being the same
    array4 = [7, 7, 7, 7, 7]
    assert selection_sort_descending(array4) == [7, 7, 7, 7, 7]

    # Test case 5: Empty array
    array5 = []
    assert selection_sort_descending(array5) == []

    # Test case 6: Array with one element
    array6 = [1]
    assert selection_sort_descending(array6) == [1]

    print("Selection sort descending test cases pass")


def test_stable_selection_sort():
    # Test case 1: Randomly generated array
    array1 = [64, 25, 12, 22, 11]
    assert stable_selection_sort(array1) == [11, 12, 22, 25, 64]

    # Test case 2: Array already sorted in ascending order
    array2 = [1, 2, 3, 4, 5]
    assert stable_selection_sort(array2) == [1, 2, 3, 4, 5]

    # Test case 3: Array sorted in descending order
    array3 = [5, 4, 3, 2, 1]
    assert stable_selection_sort(array3) == [1, 2, 3, 4, 5]

    # Test case 4: Array with all elements being the same
    array4 = [7, 7, 7, 7, 7]
    assert stable_selection_sort(array4) == [7, 7, 7, 7, 7]

    # Test case 5: Empty array
    array5 = []
    assert stable_selection_sort(array5) == []

    # Test case 6: Array with one element
    array6 = [1]
    assert stable_selection_sort(array6) == [1]

    print("Stable selection sort test cases pass")


# Running all tests
test_selection_sort_descending()
test_stable_selection_sort()
