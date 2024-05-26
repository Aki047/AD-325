import pytest

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
            has_rabbit = True
        else:
            current_Count = 0

    if not has_rabbit:
        print("No rabbits found in the list.")
    return maxRabbit_Count

# Test with a list of mixed elements including different cases of "rabbit" and other elements
# Expected outcome: 4 (since the first four elements are all "rabbit" in different cases)
def test_mixed_elements():
    assert howManyRabbits(["Rabbit", "rAbBit", "rabbit", "RABBIT", "RoCk"]) == 4

# Test with a list containing only "rabbit" in different cases
# Expected outcome: 3 (since all three elements are "rabbit" in different cases)
def test_all_rabbits():
    assert howManyRabbits(["rabbit", "RABBIT", "rAbBiT"]) == 3

# Test with an empty list to check if the correct exception is raised
# Expected outcome: ValueError with the message "The array is empty. Please update the array and try again."
def test_empty_list():
    try:
        howManyRabbits([])
    except ValueError as e:
        assert str(e) == "The array is empty. Please update the array and try again."

# Test with a list that does not contain any "rabbit"
# Expected outcome: 0 (since there are no "rabbit" elements in the list)
def test_no_rabbits():
    assert howManyRabbits(["rock", "tree", "grass", "rock", "rock"]) == 0

# Test with a list containing "rabbit" and other elements
# Expected outcome: 2 (since the maximum consecutive "rabbit" elements are two at the beginning)
def test_rabbits_and_others():
    assert howManyRabbits(["rabbit", "rabbit", "rock", "rabbit", "rock", "rock"]) == 2

# Test with a list containing consecutive "rabbit" strings interrupted by other elements
# Expected outcome: 3 (since the maximum consecutive "rabbit" elements are three at the beginning)
def test_consecutive_rabbits():
    assert howManyRabbits(["rabbit", "rabbit", "rabbit", "rock", "rabbit"]) == 3

# Test with a single "rabbit" string
# Expected outcome: 1 (since there is only one "rabbit" element)
def test_single_rabbit():
    assert howManyRabbits(["rabbit"]) == 1

# Test with multiple non-rabbit elements
# Expected outcome: 0 (since there are no "rabbit" elements in the list)
def test_multiple_non_rabbits():
    assert howManyRabbits(["rock", "tree", "grass", "bush"]) == 0

# Test with a list containing "rabbit" at the beginning and end
# Expected outcome: 2 (since the maximum consecutive "rabbit" elements are two at the end)
def test_rabbits_at_ends():
    assert howManyRabbits(["rabbit", "rock", "rock", "rabbit", "rabbit"]) == 2

# Test with a list containing special characters and "rabbit"
# Expected outcome: 1 (since only one element is exactly "rabbit" ignoring the special characters)
def test_special_characters():
    assert howManyRabbits(["rab@bit", "rabbit", "rabbi!t", "rabbit"]) == 1

if __name__ == "__main__":
    pytest.main()


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

