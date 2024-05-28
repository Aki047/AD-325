
'''
Problem: Find the longest continuous stretch of rabbits without any rocks in between


Questions:
Case sensitive
what if list is empty
What no rabbits but not empty
max or min to list size

Process:
Take list as input return the max of consecutive rabbit elements
initialized 2 variables
iterated through the list increasing the consecutive rabbit count
if the element = rock reset current_Count to 0 and move to next element
if the list larger than the max we update it with current count
Continues until all elements have been processed
after all elements have been processed, return max_RabbitCount
Error Handling
     check if the list is empty
     initial iteration covert all elements to lowercase
     return statement if no rabbits found
'''


# Test mixed elements mix of lower and upper case characters
# Tests Rabbits are at the start and end
# tEST IS EMPTY
# Test forest rabbits
# Test when elements are rocks rabbits and other items
# Test Numbers response
# Test symbols R@bbit = rabbit
# Test single element in list
# Test Consecutive non-rabbit elements followed by rabbits
# Test Alternating rabbits and non-rabbit elements

forest = ["rock", "rabbit", "rabbit", "rock", "rock", "rabbit", "rock"]

def howManyRabbits(forest):
    if not forest:
        raise ValueError('The forest is empty.')

    maxRabbit_Count = 0
    current_Count = 0
    has_rabbit = False

    for element in forest:
        if element.lower() == 'rabbit':
            current_Count += 1
            maxRabbit_Count = max(maxRabbit_Count, current_Count)
            has_rabbit = True
        else:
            current_Count = 0

    if not has_rabbit:
        print('No rabbits found, try again.')

    return maxRabbit_Count

# Test the function with the given forest
result = howManyRabbits(forest)
print("Maximum consecutive rabbits:", result)
