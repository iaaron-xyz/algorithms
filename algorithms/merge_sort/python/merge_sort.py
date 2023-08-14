def merge(left_arr: list, right_arr: list, A: list) -> None:
    """
    left_arr:  left sub-array
    right_arr:  right sub-array
    A:  original array
    
    This functions merges 2 ordered arrays L and R
    from left to right and put them into the A array
    """
    size_left: int = len(left_arr)
    size_right: int = len(right_arr)
    ith_item: int = 0
    jth_item: int = 0
    kth_item: int = 0
    # order elements left to right
    while (ith_item < size_left and jth_item < size_right):
        if left_arr[ith_item] <= right_arr[jth_item]:
            A[kth_item] = left_arr[ith_item]
            ith_item += 1
        else:
            A[kth_item] = right_arr[jth_item]
            jth_item += 1
        kth_item += 1
    # order remaining items
    for i in range(ith_item, size_left):
        A[kth_item] = left_arr[i]
        kth_item += 1
    for j in range(jth_item, size_right):
        A[kth_item] = right_arr[j]
        kth_item += 1


def merge_sort(A: list) -> None:
    """
    A: array to be sorted

    This function receives an array A and
    order it in place using the merge sort algorithm.
    if returns 0, the arrays has been sorted succesfully.
    """
    size: int = len(A)
    # Do nothing if the array has 1 or less elements
    if size < 2: return
    # array size parameters
    mid: int = size//2
    left: int = A[0:mid]
    right: int = A[mid:]
    # sort and merge
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)
    return 0

# Test
A: list = [4,6,7,2,100,1,5,3,22,47,15,2]
B: list = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]

print(f'A - Before: {A}')
merge_sort(A)
print(f'A - After: {A}')
print(20*"-")
print(f'B - Before: {B}')
merge_sort(B)
print(f'B - After: {B}')