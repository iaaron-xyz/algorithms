def calculate_pi(n_terms: int) -> float:
    """(int) -> float
    This function computes the number pi using the Leibniz formula.
    pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

    Receives an integer, being the number of terms to use in the Liebniz
    formula.
    Returns a float, being pi.
    """
    numerator: float = 4.0
    denominator: float = 1.0
    sign: float = -1.0
    pi: float = 0
    for i in range(n_terms):
        pi += ((sign)**i) * (numerator / denominator)
        denominator += 2.0
    return pi

if __name__ == "__main__":
    print(calculate_pi(100000)) # 3.1415826535897198