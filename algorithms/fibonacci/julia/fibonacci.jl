function fibArr(n, s=Array{BigInt}([0,1]))
    #=
    (int, arr) -> arr
    =#
    # base case: return the array with n elements
    if length(s) > n
        return s[1:n+1]
    end
    # rcursive case: Add one more element
    return fibArr(n, append!(s, [s[end] + s[end-1]]))
end

memo = Dict{Int64, BigInt}(0=>0, 1=>1)
function fib(n)
    # remember every number that is different
    if !(haskey(memo, n))
        memo[n] = fib(n-1) + fib(n-2)
    end
    # contained element
    return memo[n]
end

# println(fibArr(0))
# println(fibArr(1))
# println(fibArr(2))
# println(fibArr(5))
# println(fibArr(10))
# println(fibArr(20))

# println(fib(0))
# println(fib(1))
# println(fib(2))
# println(fib(5))
# println(fib(10))
# println(fib(20))

# Dealing with big numbers
# println(fibArr(BigInt(100)))
# println(fib(BigInt(100)))