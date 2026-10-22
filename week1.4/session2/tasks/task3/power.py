# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.


def power(x, n):
    # complete your code here
    # base case

    # recursive case
    if n == 0:
        return 1
    return x * power(x, n - 1)


# Once completed, make at least two function calls to test the power function
print(power(2, 3))  # Output: 8
print(power(5, 2))  # Output: 25