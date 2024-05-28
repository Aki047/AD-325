from Rabbit_Count import howManyRabbits

# Test case 1: Mixed elements with different cases
forest1 = ["Rabbit", "rAbBit", "rabbit", "RABBIT", "RoCk"]
assert howManyRabbits(forest1) == 4

# Test case 2: Rabbits are at the start and end
forest2 = ["rabbit", "rock", "rock", "rabbit", "rabbit"]
assert howManyRabbits(forest2) == 2

# Test case 3: Empty forest
forest3 = []
try:
    howManyRabbits(forest3)
except ValueError as e:
    assert str(e) == 'The forest is empty.'

# Test case 4: Forest with all rabbits
forest4 = ["rabbit", "rabbit", "rabbit"]
assert howManyRabbits(forest4) == 3

# Test case 5: Elements are rocks, rabbits, and other items
forest5 = ["rabbit", "rock", "rabbit", "tree", "rabbit"]
assert howManyRabbits(forest5) == 1

# Test case 6: Special characters treated as non-rabbit
forest7 = ["rab@bit", "rabbit", "rabbi!t", "rabbit"]
assert howManyRabbits(forest7) == 1

# Test case 7: Single element rabbit
forest8 = ["rabbit"]
assert howManyRabbits(forest8) == 1

# Test case 8: Consecutive non-rabbit elements followed by rabbits
forest9 = ["rock", "rock", "rabbit", "rabbit", "rabbit"]
assert howManyRabbits(forest9) == 3

# Test case 9: Alternating rabbits and non-rabbit elements
forest10 = ["rabbit", "rock", "rabbit", "rock", "rabbit"]
assert howManyRabbits(forest10) == 1

print("All tests passed!")
