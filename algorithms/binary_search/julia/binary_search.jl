function binary_search(list, item)
    # initial values
    low = 0
    high = length(list)

    while low <= high
        # element guess
        mid = (low + high) ÷ 2
        guess = list[mid]
        println("Guess: ", mid)
        #found
        if guess == item
            return mid
        end
        # discard upper half
        if guess > item
            high = mid - 1
        else
            low = mid + 1
        end
        
    end
end

println(binary_search([1,3,4,5,7,8,11,234], 234))
println(binary_search([1,3,4,5,7,8,11,234], 7))