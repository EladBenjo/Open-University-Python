""""
by @Elad_Benjo May 2025
The Open University of Israel
"""

def find_max(lst):
    """
    Finds the maximum value in a rotated sorted list in O(log n) time.

    The list is assumed to be originally sorted in increasing order,
    and then rotated at some unknown pivot. For example:
        [5, 6, 7, 1, 2, 3, 4]
    is a rotated version of [1, 2, 3, 4, 5, 6, 7].

    This function uses a recursive approach that compares the maximum
    values at the edges of each half of the list, and proceeds to the
    half that contains the larger edge value. The process continues
    until a single element is left, which must be the maximum.

    :param lst: List[int] - a rotated sorted list of unique integers
    :return: int or str - the maximum value in the list, or "None" if empty
    """

    def helper(lst, start, end):
        # Base case: only one element left
        if start <= end:
            if start == end:
                return lst[start]

            # Compute the midpoint of the current sublist
            mid = (start + end) // 2

            # Get the maximum value between start and mid (left side)
            left = max(lst[start], lst[mid])

            # Get the maximum value between mid+1 and end (right side)
            right = max(lst[mid + 1], lst[end])

            # Recur into the half with the larger boundary value
            if left > right:
                return helper(lst, start, mid)
            else:
                return helper(lst, mid + 1, end)

        # Empty list or invalid range
        return "None"

    # Handle empty list case
    if lst:
        return helper(lst, 0, len(lst) - 1)
    return "None"

def find_pairs(lst, k):
    """
    Counts the number of unique pairs (a, b) in a sorted list such that b - a == k and a < b.

    Since the list is sorted in ascending order and contains unique values,
    we can use a two-pointer technique to find valid pairs efficiently:

    - Start with two pointers, i and j (initially i=0, j=1).
    - At each step, calculate the difference: diff = lst[j] - lst[i].
    - If diff < k → move j forward (to increase the difference).
    - If diff > k → move i forward (to decrease the difference).
    - If diff == k → count the pair and move both pointers forward.
    - Make sure i < j at all times to avoid using the same element twice.

    This results in an efficient O(n) solution, leveraging the sorted nature of the list.

    :param lst: List[int] - sorted list of unique integers
    :param k: int - the exact difference to find between values
    :return: int - number of valid (a, b) pairs such that b - a == k
    """
    count = 0
    i, j = 0, 1
    n = len(lst)

    while j < n:
        # Ensure i and j are not pointing to the same element
        if i == j:
            j += 1
            continue

        diff = lst[j] - lst[i]

        if diff < k:
            # Difference too small, move j to the right to increase it
            j += 1
        elif diff > k:
            # Difference too big, move i to the right to reduce it
            i += 1
        else:
            # Found a valid pair (a, b) such that b - a == k
            count += 1
            i += 1
            j += 1

    return count

def update_list(lst, value):
    """
    Recursively removes the first occurrence of 'value' from the list 'lst'.
    If 'value' is not found in the list, the list is returned unchanged.

    This function acts as a wrapper and calls a helper function
    with an index parameter to track position during recursion.

    :param lst: List[int] - a list of integers
    :param value: int - the value to remove (first occurrence only)
    :return: List[int] - a new list with the first occurrence of value removed
    """
    return update_list_helper(lst, value, 0)

def update_list_helper(lst, value, i):
    """
    Helper function that performs the recursive search and removal.

    :param lst: List[int] - the list to process
    :param value: int - the value to remove
    :param i: int - current index in recursion
    :return: List[int] - updated list with first 'value' removed if found
    """
    if lst:
        # Check if current element matches the value to remove
        if lst[i] == value:
            # Remove the element by slicing and return the new list
            result = lst[:i] + lst[i+1:]
            return result
        # If reached the end of the list without finding the value
        elif i + 1 >= len(lst):
            return lst
        else:
            # Continue searching recursively
            return update_list_helper(lst, value, i + 1)
    # Return original list if it's empty
    return lst


def equal_lists(lst1, lst2):
    """
    Recursively checks whether two lists of integers contain the same elements
    with the same number of occurrences, regardless of order.

    The function removes each element from lst1 one by one,
    and attempts to remove the same element from lst2 using update_list.
    If all elements are successfully matched and removed, the lists are equal.

    :param lst1: List[int] - first list of integers
    :param lst2: List[int] - second list of integers
    :return: bool - True if both lists contain the same elements with the same counts, else False
    """
    # Both lists are empty → they match
    if lst1 == lst2 == []:
        return True
    # One list is empty and the other is not → mismatch
    elif lst1 == [] or lst2 == []:
        return False
    else:
        # Try to remove lst1[0] from lst2 (only once)
        lst2 = update_list(lst2, lst1[0])
        # Continue recursively with the rest of lst1
        return equal_lists(lst1[1:], lst2)

def is_palindrome(lst):
    """
    Recursively checks whether:
    1. All strings in the list are palindromes.
    2. The list itself is a palindrome (i.e., reads the same forwards and backwards).

    :param lst: List of strings
    :return: True if all strings are palindromes and the list is a palindrome, else False
    """
    if len(lst) <= 1:
        # Base case: If list is empty or has one element,
        # check that the single element (if exists) is a palindrome.
        if lst and not string_is_palindrome(lst[0]):
            return False
        else:
            return True
    elif lst[0] != lst[-1] or not string_is_palindrome(lst[0]):
        # If the list is not symmetric, or the first string is not a palindrome
        return False
    else:
        # Recursive step: check the sublist without the first and last elements
        return is_palindrome(lst[1:-1])

def string_is_palindrome(string):
    """
    Recursively checks whether a given string is a palindrome.

    :param string: A string to check
    :return: True if the string is a palindrome, else False
    """
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        # Recursive step: check the substring without the first and last characters
        return string_is_palindrome(string[1:-1])


