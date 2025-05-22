""""
by @Elad_Benjo May 2025
The Open University of Israel
"""


import copy


def complement(lst):
    """
    Return the complement list of integers not present in the input list.

    This function checks all integers from 1 up to (but not including) the maximum value in lst.
    Any number within that range that does not exist in lst is added to the complement list.

    Args:
        lst (list of int): A list of positive integers.

    Returns:
        list of int: A list containing the missing integers between 1 and max(lst) - 1.
    """
    lst_comp = []

    if lst:
        for i in range(1, max(lst)):
            exist = False
            for j in lst:
                if i == j:
                    exist = True
                    break  # Stop searching if value is found
            if not exist:
                lst_comp.append(i)

    return lst_comp


def shift_k_right(lst, k):
    """
    Shift the list k positions to the right (circularly).

    Args:
        lst (list): List to be shifted.
        k (int): Number of positions to shift. Must be between 0 and len(lst).

    Returns:
        list: The shifted list.

    Raises:
        ValueError: If k is not in the valid range.
    """
    if k < 0 or k > len(lst):
        raise ValueError("k must be between 0 and lst length!")

    return lst[-k:] + lst[:-k]


def shift_right_size(a, b):
    """
    Return the shift size needed to transform list b into list a using right shifts.

    Args:
        a (list): Target list.
        b (list): Original list to be shifted.

    Returns:
        int or str: The number of right shifts needed to match a, or "None" if not possible.
    """
    if a and b:
        if a == b:
            return 0
        for i in range(1, len(b)):
            if shift_k_right(b, i) == a:
                return i
    return "None"


def is_valid(val, lst):
    """
    Validate that a value is an integer and within the bounds of a list.

    Args:
        val (any): Value to validate.
        lst (list): List for index bounds.

    Raises:
        TypeError: If val is not an integer.
        IndexError: If val is out of list bounds.
    """
    if not isinstance(val, int):
        raise TypeError("Val must be an Int type!")
    if val < 0 or val >= len(lst):
        raise IndexError("The value " + str(val) + " is out of the array boundaries")


def is_perfect(lst):
    """
    Determine if a list forms a perfect sequence.

    The sequence starts at index 0, and at each step jumps to the value at the current index.
    A perfect list visits all indices and ends by looping or reaching 0.

    Args:
        lst (list): List of integers.

    Returns:
        bool: True if list is perfect, False otherwise.
    """
    result = True

    if lst:
        test = [0] * len(lst)
        val = 0
        done = False

        while not done:
            test[val] = 1
            val = lst[val]
            is_valid(val, lst)
            if val == 0 or val == lst[val]:
                done = True

        for i in range(len(test)):
            if test[i] == 0:
                result = False

    return result


def identity_matrix(mat):
    """
    Check if a matrix is an identity matrix.

    An identity matrix has 1s on the main diagonal and 0s elsewhere.

    Args:
        mat (list of list of int): 2D square matrix.

    Returns:
        bool: True if mat is an identity matrix, False otherwise.

    Raises:
        TypeError: If a non-integer value is found.
    """
    if mat:
        row_length = len(mat)
        column_length = len(mat[0])

        if row_length != column_length:
            return False

        for i in range(row_length):
            for j in range(column_length):
                if not isinstance(mat[i][j], int):
                    raise TypeError("Not all values are int!")
                # check the main diagonal
                if i == j:
                    if mat[i][j] != 1:
                        return False
                # check cells that are not in the main diagonal
                else:
                    if mat[i][j] != 0:
                        return False

    return True


def create_sub_matrix(mat, size):
    """
    Extract a centered sub-matrix of the given size from mat.

    Args:
        mat (list of list of int): Original 2D matrix.
        size (int): Size of the desired sub-matrix.

    Returns:
        list of list of int: Centered sub-matrix.

    Raises:
        IndexError: If matrix is not square or not of odd size.
    """
    sub_matrix = []

    if mat:
        if len(mat) % 2 == 0:
            raise IndexError("The matrix must be odd")

        # check all rows and columns same length
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise IndexError("Matrix rows must have equal length")

        # find the center and adjust offset to use from both sides
        center = len(mat) // 2
        offset = size // 2

        for i in range(center - offset, center + offset + 1):
            row = []
            for j in range(center - offset, center + offset + 1):
                row.append(mat[i][j])
            sub_matrix.append(row)

    return sub_matrix


def max_identity_matrix(mat):
    """
    Return the size of the largest centered sub-matrix within mat that is an identity matrix.

    Args:
        mat (list of list of int): 2D matrix to search within.

    Returns:
        int: Size of the largest identity sub-matrix found.
    """
    max_mat = []

    if mat:
        max_size = len(mat)

        # iterate from the outer layer of the mat inside and search for identity matrix
        for size in range(max_size, 0, -1):
            try:
                sub_matrix = create_sub_matrix(mat, size)
                if sub_matrix and identity_matrix(sub_matrix):
                    max_mat = copy.deepcopy(sub_matrix)
                    break
            except TypeError as e:
                print(f"TypeError caught: {e}")
                return 0

    return len(max_mat)
