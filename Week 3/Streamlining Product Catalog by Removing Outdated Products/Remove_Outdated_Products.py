'''
Problem Statement: write a program that removes all occurrences of a specified product (represented by an ID) from the company's product catalog array. The program should modify the array in place and return the count of remaining products.

The task involves removing all instances of a given product ID (discontinuedID) from the product catalog array (productCatalog).

Q's
Can the productCatalog array contain duplicate product IDs, and should all duplicates be removed?
Are the product IDs in the productCatalog sorted or unsorted?
How should the function handle cases where the discontinuedID is not present?

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

    # is discontinuedID was present in the catalog
    if not foundDiscontinued:
        print("Warning: Discontinued product ID was not found in the catalog.")

    # Clear the remaining elements
    for i in range(writer, len(productCatalog)):
        productCatalog[i] = None  # Assuming clearing with None is acceptable

    return writer  # The writer's position also represents the count of remaining products


# Example usage
productCatalog1 = [1003, 1002, 1002, 1003]
discontinuedID1 = 1003
print("Remaining count:", Discontinued_Products(productCatalog1, discontinuedID1), ", Updated Catalog:",
      productCatalog1)

