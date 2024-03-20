


import math

def howManyLegs(animals, four_Legs):
    if not animals:
        raise ValueError("The input array is empty. Please provide a non-empty array.")

    animalCount = 0
    has_four_legged_animal = False  # Flag to check if at least one four-legged animal is found

    for animal in animals:
        if animal in four_Legs:  # Check if the animal is in the list of four-legged animals
            animalCount += 1
            has_four_legged_animal = True

    if not has_four_legged_animal:
        print("There are no four-legged animals in the array.")

    return animalCount

animals = ['lion', 'monkey', 'snake', 'deer', 'elephant']
four_Legs = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']
two_Legs = ['monkey', 'parrot', 'ostrich']
zero_Legs =['snake', 'worm']
multiple_Legs = ['spider', 'ant', 'centipede']

result = howManyLegs(animals, four_Legs)
print(result)

'''
Process
iterate through array, check if in four_Legs, if in four_legs +1 to animal count
return and print animalCount

Questions:
What if array empty
is it case sensitive
if no fourlegged animals what return
do we need to account for specific category of animals
if so scaleablity for other leg counts
'''
