import math


def compute_factorial(n):
    """Computes the factorial for argument n
    example: compute_factorai(3) returns 6

    pre-condition: n must be a non-negative
    post-condition: results will be a non-negative integer

    note: non-integers are not supported. any non-integer arguments
          will be converted to integers.
    """
    if n < 0:
        return -1 # don't want an infinite loop

    if n > 1:
        # recursion: call ourselves for n-1 case
        return compute_factorial(n-1)*(n-1)

    if n == 1:
        return 1

    
    



# write unti tests here

