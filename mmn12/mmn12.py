""""
by @Elad_Benjo April 2025
The Open University of Israel
"""

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): A natural number greater than 1.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def max_prime():
    """
    Read numbers from user input until a number less than 1 is entered.
    Return the maximum prime number from the inputs.
    If no prime numbers were entered, return 1.

    Returns:
        int: The largest prime number entered, or 1 if none were prime.
    """
    primes = []
    while True:
        n = int(input("Enter a number (less than 1 to stop): "))
        if n < 1:
            break
        if is_prime(n):
            primes.append(n)

    return max(primes) if primes else 1


def compression(s):
    """
    Compress a string using a basic run-length encoding algorithm.

    For each sequence of repeated characters, store the character followed by the count.
    If a character appears only once, it is stored without a count.

    Args:
        s (str): The original string to compress.

    Returns:
        str: The compressed string.
    """
    result = ""
    count = 1

    for i in range(len(s)):
        # Check if next character is the same
        if (i + 1) < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i]
            if count > 1:
                result += str(count)
            count = 1  # Reset for the next character

    return result


def sum_square(num):
    """
    Calculate the sum of the squares of the digits of a number.

    Args:
        num (int): A natural number.

    Returns:
        int: Sum of squares of the digits of num.
    """
    result = 0
    while num > 0:
        digit = num % 10
        result += digit ** 2  # Add square of the last digit
        num = num // 10       # Remove last digit
    return result


def is_happy(num):
    """
    Determine if a number is a 'happy number'.

    A happy number is one where the repeated process of replacing the number
    with the sum of squares of its digits eventually reaches 1.
    The process stops after 10 steps. If 1 is not reached, the number is not happy.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is happy, False otherwise.
    """
    count = 0
    while num != 1:
        num = sum_square(num)
        count += 1
        if count == 10:
            return False
    return True


def count_happy_numbers():
    """
    Count how many happy numbers exist between 1 and 100 (inclusive).

    Returns:
        int: The number of happy numbers between 1 and 100.
    """
    happy_numbers_count = 0
    for i in range(1, 101):
        if is_happy(i):
            happy_numbers_count += 1
    return happy_numbers_count
