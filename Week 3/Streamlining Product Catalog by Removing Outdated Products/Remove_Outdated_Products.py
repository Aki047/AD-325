'''
Problem Statement: write a program that removes all occurrences of a specified product (represented by an ID) from the company's product catalog array. It should modify the array in place and return the count of remaining products.

The task involves removing all instances of a given product ID (discontinuedID) from the product catalog array (productCatalog).

Process: 
Define function
Initialize variables set writer to 0 & foundDiscontinued to false
go through catalog, Loop through each product ID in productCatalog using a for loop.
If the current product ID matches discontinuedID, set foundDiscontinued to True.If it does not match, write the current product ID to the position indicated by writer and increment writer.
Check for discontinuedID
Clear remaining elements
Return the Count of Remaining Products:

Q's:
Can the productCatalog array contain duplicate product IDs, and should all duplicates be removed?
Are the product IDs in the productCatalog sorted or unsorted?
How should the function handle cases where the discontinuedID is not present?

Time and Space Complexity:
Time Complexity: O(n), Iterates exactly once for each element
Space Complexity: O(1), modifies the list in place and does not use any additional data structures

'''

def Discontinued_Products(productCatalog, discontinuedID):
    # Validate the input data
    if not isinstance(productCatalog, list) or not isinstance(discontinuedID, int):
        print("Error: Invalid input data types.")
        return -1  # Indicating an error condition

    if not productCatalog:
        print("The product catalog is empty.")
        return 0  # No products to process

    writer = 0  # Pointer writes values not equal to discontinuedID
    foundDiscontinued = False  # Flag to check if discontinuedID is found

    for reader in range(len(productCatalog)):
        if productCatalog[reader] == discontinuedID:
            foundDiscontinued = True
        else:
            productCatalog[writer] = productCatalog[reader]
            writer += 1

    # Check if discontinuedID was present in the catalog
    if not foundDiscontinued:
        print("Warning: Discontinued product ID was not found in the catalog.")

    # Clear the remaining elements
    for i in range(writer, len(productCatalog)):
        productCatalog[i] = None  # Assuming clearing with None is acceptable

    return writer  # The writer's position also represents the count of remaining products
