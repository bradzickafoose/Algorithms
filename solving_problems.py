# Print the factorial of n


def rec_factorial(n):
    print(n)
    # base case
    if n <= 1:
        return 1

    # recursive steps
      # prev = rec_factorial(n-1)
      # return n * prev
    return n * rec_factorial(n-1)


rec_factorial(5)
