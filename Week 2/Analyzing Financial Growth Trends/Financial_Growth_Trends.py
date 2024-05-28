'''
Purpose:
Write a program that models growth trends based on historical financial data. Specifically, when given an array of financial growth percentages (which may include negative values representing a decrease). You need to return an array of the growth trends squared, sorted in non-decreasing order, simulating a real-world business data analysis scenario.

Process:
iterate through growthPercentages array square each element
append each squared element to new array
sort array in non-decreasing order
print statement f"After squaring the array becomes {squaredPercentages}. After sorting, it becomes{squaredPercentages.sorted}"

Questions:
what if array empty, what will the output be
array maximum or minimum
what if data type is wrong, error validation on string
supports just floating and int or only int4
'''
import math
import numpy as np

def financialGrowthTrends(growthPercentages):
    #if not growthPercentages:
     #   return []  # Return an empty list for an empty input array

    if not growthPercentages:
        raise ValueError("The input array is empty. Please provide a non-empty array.")

    if not all(isinstance(x, (int, float)) for x in growthPercentages):
        raise ValueError("The input array should contain only numeric values (int or float).")

    squaredGrowthPercentages = np.power(growthPercentages, 2)
    squaredGrowthPercentages.sort()  # Sort the squared percentages in non-decreasing order

    return squaredGrowthPercentages

growthPercentages = [-5, -2, 0, 3, 10]

result = financialGrowthTrends(growthPercentages)

print(f"After squaring, the array becomes {result}. After sorting, it becomes {result.tolist()}.")

'''
Time Complexity
o(n) check for num values in array
o(n) squaring each element
o(n log n) overall time complexity

Space Complexity:
O(n) using additional space to store

Test Case:
empty input
non-numeric values
single
postive only
negative only
mixed values
duplicates
floating values

'''