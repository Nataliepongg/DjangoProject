def is_prime(n):
    # Check for non-positive integers
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    #special case when n is 1
    if (n==1):
        return False

    # Check for prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True