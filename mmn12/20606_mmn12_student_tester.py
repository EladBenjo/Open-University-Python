# place your mmn12 functions here

def main():
    """
    Tester for all functions in the assignment.
    Calls each function with multiple test cases and prints the results.
    """
    print("Question 1: Prime Number Functions")
    print("Testing is_prime:")
    print("is_prime(7):", is_prime(7))  # Expected: True
    print("is_prime(10):", is_prime(10))  # Expected: False

    print("\nTesting max_prime:")
    # Since max_prime requires user input, it should be tested manually
    print("Please test max_prime function manually due to input requirements.")

    print("\nQuestion 2: Compression Function")
    print("Testing compression:")
    print("compression('aabccceeeeedab'):", compression("aabccceeeeedab"))  # Expected: a2bc3e5dab
    print("compression('abcde'):", compression("abcde"))  # Expected: abcde
    print("compression('xxxyyyzzz'):", compression("x3y3z3"))  # Expected: x3y3z3

    print("\nQuestion 3: Happy Numbers")
    print("Testing sum_square:")
    print("sum_square(123):", sum_square(123))  # Expected: 14
    print("sum_square(98):", sum_square(98))  # Expected: 145

    print("\nTesting is_happy:")
    print("is_happy(19):", is_happy(19))  # Expected: True
    print("is_happy(2):", is_happy(2))  # Expected: False

    print("\nTesting count_happy_numbers:")
    print("count_happy_numbers():", count_happy_numbers())  # Expected: 20


if __name__ == "__main__":
    main()