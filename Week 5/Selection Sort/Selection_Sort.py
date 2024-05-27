def selection_sort(array):
    length = len(array)

#Outter Loop iterates through the array In each iteration, the value of the variable i is assigned to the variable
    for i in range(length - 1):
        minIndex = i
#Inner Loop compares the value held at the index of i updating Only unsorted values are picked
        for j in range(i + 1, length):
            if array[j] > array[minIndex]:
                maxIndex = j
        array[i], array[maxIndex] = array[maxIndex], array[i]

    return array


print("The sorted array is: ", selection_sort(array))