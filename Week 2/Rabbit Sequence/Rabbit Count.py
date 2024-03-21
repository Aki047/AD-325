def howManyRabbits(forest):
    if not forest:
        raise ValueError("The array is empty. Please update the array and try again.")

    maxRabbit_Count = 0
    current_Count = 0
    has_rabbit = False

    for element in forest:
        if element.lower() == 'rabbit':
            current_Count += 1
            maxRabbit_Count = max(maxRabbit_Count, current_Count)
        else:
            current_Count = 0

    if has_rabbit:
        print("No rabbits found in the list.")
    return maxRabbit_Count

forest= ["Rabbit", "rAbBit", "rabbit", "RABBIT", "RoCk"]
result = howManyRabbits(forest)
print(result)

# Example forest lists
forest_with_rabbits = ["rabbit", "rabbit", "rock", "rabbit", "rock", "rock"]
forest_without_rabbits = ["rock", "tree", "grass", "rock", "rock"]

# Demonstrating the function with a list that includes rabbits
result_with_rabbits = howManyRabbits(forest_with_rabbits)
print("Maximum consecutive rabbits (with rabbits):", result_with_rabbits)

# Demonstrating the function with a list that does not include rabbits
result_without_rabbits = howManyRabbits(forest_without_rabbits)
print("Maximum consecutive rabbits (without rabbits):", result_without_rabbits)

'''
Process
initlized the two variables to keep track of counting
iterated through array increasing current count when rabbit is encountered, if current count is larger than maxRabbit_count then updating max_RabbitCount
if the element = rock reset current_Count to 0 and move to next element
continue until all elements have been processed
after all elements have been processed, return max_RabbitCount

Error Handling
     initial iteration covert all elements to lowercase
'''

