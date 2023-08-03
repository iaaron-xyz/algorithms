
# Find the smallest element in an array
# and return its index
#######################################
def find_smallest(arr: list) -> int:
    """(array) -> int
    Given list as an input, return the index of
    the smallest element.
    """
    # Store the smallest value
    smallest: int = arr[0]
    # store the index of the smallest value
    smallest_index: int = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# Selection sort
#######################################
def selection_sort(arr: list) -> list:
    """(array) -> int
    Sort the elements of the input array.
    Returns a new array with those sorted elements.
    """
    # new array with sorted elements
    sorted_arr: list = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


# Example
print(selection_sort([6, 2, 7, 11, 4, 2]))
