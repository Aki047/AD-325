'''

Assignment: Inventory Management System Update

Problem Statement: Inventory Management System Update
given an array representing the stock count of different products in a store. Each occurrence of zero represents a product that is out of stock. Duplicate each occurrence of zero (indicating an order placed to restock that product), shifting the remaining product counts to the right.

Questions
Should we consider scenarios where the input array is empty?
How should we handle cases where there are consecutive zeros in the inventory?
Are there any constraints on the size of the input array or the values within it?


Process

Check for Empty Input Array:
Before processing, check if the input inventory array is empty. If it is, return without performing any modifications.

Iterate through the inventory array to calculate the available slots for potential zero duplications.This ensures that we don't exceed the length of the array during duplication.

Duplicate Zeros:
Iterate through the inventory array in reverse order.
If a zero is encountered and there are available slots (zeros_to_duplicate > 0):
Shift the subsequent elements to the right by the number of available slots (zeros_to_duplicate) to make space for duplicated zeros.
Decrement zeros_to_duplicate to track the remaining available slots.
If zeros_to_duplicate is zero or negative, simply shift the subsequent elements to the right to maintain array integrity.
If the current element is not zero, continue without modification.
'''

import copy

def duplicateZeros(inventory):
    # Check if the inventory array is empty
    if not inventory:
        print("Input array is empty. Please provide a non-empty array.")
        return [], []  # Handle empty input array

    # Count the number of zeros in the inventory array
    zeros_to_duplicate = inventory.count(0)
    length = len(inventory)
    available_slots = length

    # Calculate available slots considering consecutive zeros
    for i in range(length):
        available_slots -= 1
        # Check if the current element is zero and if there are enough available slots for duplication
        if inventory[i] == 0 and available_slots <= zeros_to_duplicate:
            zeros_to_duplicate -= 1

    # Make a shallow copy of the original inventory
    modified_inventory = inventory[:]

    # Loop through the inventory array in reverse order to duplicate zeros
    for i in range(length - 1, -1, -1):
        if inventory[i] == 0:
            if zeros_to_duplicate > 0:
                # Insert a zero at the appropriate position to duplicate it
                modified_inventory.insert(i + zeros_to_duplicate, 0)
                zeros_to_duplicate -= 1
            else:
                # Insert a zero at the appropriate position to ensure the correct array length
                modified_inventory.insert(i + zeros_to_duplicate, 0)

    # Print the modified and original inventories
    print("Inside duplicateZeros function:")
    print("Modified Inventory:", modified_inventory)
    print("Original Inventory:", inventory)

    # Return the modified inventory and the original inventory
    return modified_inventory, inventory


# Test cases
inventory = [4, 0, 1, 3, 0, 2, 5, 0]
modified_inventory, original_inventory = duplicateZeros(inventory)
print("Outside duplicateZeros function:")
print("Modified Inventory:", modified_inventory)
print("Original Inventory:", original_inventory)


# Test cases
inventory = [4, 0, 1, 3, 0, 2, 5, 0]
modified_inventory, original_inventory = duplicateZeros(inventory)
print("Outside duplicateZeros function:")
print("Modified Inventory:", modified_inventory)
print("Original Inventory:", original_inventory)


