def binary_search(arr: list, item: int) -> int:
    """(arr, str) -> int
    This functions search for the element item in the
    array arr.
    If found, returns its index position, else returns None.
    """
    # initial values
    low: int = 0
    high: int = len(arr)-1

    while low <= high:
        # guess the middle element
        mid: int = (low + high)//2
        guess: int = arr[mid]
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

    return

print(binary_search([1,3,4,5,7,8,11,234], 234))
print(binary_search([1,3,4,5,7,8,11,234], 3))