import math

'''
Steps for resolution:
iterate through growthPercentages array square each element
#append each squared element to new array
#sort array in non-decreasing order
print statement f"After squaring the array becomes {squaredPercentages}. After sorting, it becomes{squaredPercentages.sorted}"

Clarifying questions: 
what if array empty
array maximum or minimum 
what if data type is wrong, error validation on string


'''

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

