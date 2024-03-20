import math



def howManyRabbits (forest):

if not forest:
    raise ValueError("The array is empty. Please update array and try again")

    maxRabbit_Count = 0

    current_Count = 0

    has_rabbit = False # check forest for at least one rabbit

    for element in forest:
        element = element.lower();


        if element == 'rabbit':
            current_Count =+1
            maxRabbit_Count = max(maxRabbit_Count, current_Count)
        else:
            current_Count = 0

    return maxRabbit_Count

forest = ["rabbit, rabbit, rock, rabbit, rock rock"]

result = howManyRabbits(forest)
print(result)

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

