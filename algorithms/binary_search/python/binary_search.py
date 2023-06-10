def binary_search(list, item):
    """(list, str) -> int
    This functions search for the element item in the
    array list.
    If found, returns its index position, else returns None.
    """
    # initial values
    low = 0
    high = len(list)-1

    while low <= high:
        # guess the middle element
        mid = (low + high)//2
        guess = list[mid]
        print(f'Index guess: {mid}')
        # found
        if guess == item:
            return mid
        # discard upper half
        if guess > item:
            high = mid - 1
        # discard lower half
        else:
            low = mid + 1

print(binary_search([1,3,4,5,7,8,11,234], 234))
print(binary_search([1,3,4,5,7,8,11,234], 3))