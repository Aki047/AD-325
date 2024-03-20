def ITMS(inventory):
    # Count the zeros in the inventory
    zero_count = inventory.count(0)

    # The length of the inventory we need to consider after accounting for the shifts
    # caused by duplicating zeros
    length_to_consider = len(inventory) - zero_count

    # Iterate backwards from the end of the array we need to consider, shifting and duplicating zeros
    for i in range(length_to_consider - 1, -1, -1):
        if i + zero_count < len(inventory):
            inventory[i + zero_count] = inventory[i]
        # If the current element is a zero, decrement zero_count and set the duplicated zero if within bounds
        if inventory[i] == 0:
            zero_count -= 1
            if i + zero_count < len(inventory):
                inventory[i + zero_count] = 0

# Examples
inventory = [4,0,1,3,0,2,5,0]
ITMS(inventory)
print(inventory)

# Expected output: [4,0,0,1,3,0,0,2]

# Another example
inventory2 = [3,2,1]
ITMS(inventory2)
print(inventory2)
# Expected output: [3,2,1]
