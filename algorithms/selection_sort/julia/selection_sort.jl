"""
    findSmallest(x)
x: must be an array.
Returns: int -> index

Returns the `index` of the element of the array with the
lower value. If this value is repeated, returns the first one.
If the array is empty returns `-1`
"""
function find_smallest(arr)
    # Store the smallest element
    smallest = arr[1]
    # Store the index of the smallest element
    smallest_index = 1
    for i in eachindex(arr)
        if arr[i] < smallest
            smallest = arr[i]
            smallest_index = i
        end
    end
    return smallest_index
end


"""
    selection_sort(x)
x: array
return: array

This function receives an array and sorts it using the selection sort
algorithm. Returns a new created array as result.
"""
function selection_sort(arr)
    sorted_arr = []
    for i in 1:length(arr)
        smallestIndex = find_smallest(arr)
        push!(sorted_arr, arr[smallestIndex])
        splice!(arr, smallestIndex)
    end
    return sorted_arr
end


# Usage example
println(selection_sort([6,2,7,11,4,2]))