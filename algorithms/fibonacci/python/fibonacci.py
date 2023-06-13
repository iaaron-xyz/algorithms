def fibArr(n, s=[0,1]):
    """(int, arr) -> arr
    Returns an array containing the first n+1 fibonacci numbers.
    This function is computed recursively.
    """
    # return the n elements in an array
    if (len(s) > n):
        return s[0:n+1]
    # add the next number to the sequence
    return fibArr(n, s+[s[-2] + s[-1]])


from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    """(int) -> int
    Returns an integer, being the nth fibonacci number.
    This function is computed recursively and make use of
    the decorator @functools.lru_cache().
    """
    # base case
    if n < 2:
        return n
    # recursive case
    return fib(n-1) + fib(n-2)



# print(fibArr(0))
# print(fibArr(1))
# print(fibArr(2))
# print(fibArr(5))
# print(fibArr(10))
# print(fibArr(20))

# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(5))
# print(fib(10))
# print(fib(20))
