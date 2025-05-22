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
        # check all rows and columns same length
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise IndexError("Not all rows are equal")

        if len(mat) % 2 == 0:
            raise IndexError("The matrix must be odd")



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

def print_result(desc, result):
    print(f"{desc}: {result}")


def test_complement():
    print("\n--- Testing complement ---")
    print_result("Test 1", complement([9, 8, 7, 5, 4, 1]))  # [2, 3, 6]
    print_result("Test 2", complement([1, 4, 2, 3]))        # []
    print_result("Test 3", complement([]))                  # []
    print_result("Test 4", complement([2, 4, 6]))           # [1, 3, 5]
    print_result("Test 5", complement([10, 1]))             # [2, 3, 4, 5, 6, 7, 8, 9]


def test_shift_k_right():
    print("\n--- Testing shift_k_right ---")
    print_result("Test 1", shift_k_right([1, 2, 3, 4, 5], 3))  # [3, 4, 5, 1, 2]
    print_result("Test 2", shift_k_right([1, 2, 3, 4, 5], 1))  # [5, 1, 2, 3, 4]
    try:
        shift_k_right([1, 2], 5)  # Should raise ValueError
    except ValueError as e:
        print_result("Test 3", f"Exception caught: {e}") # Exception caught: ...


def test_shift_right_size():
    print("\n--- Testing shift_right_size ---")
    a = [4, -1, 9, 7, 11, 2]
    b = [11, 2, 4, -1, 9, 7]
    print_result("Test 1", shift_right_size(a, b))  # 4

    c = [4, -1, 9, 7, 11, 2]
    d = [4, -1, 7, 9, 11, 2]
    print_result("Test 2", shift_right_size(c, d))  # None

    print_result("Test 3", shift_right_size([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # 0
    print_result("Test 4", shift_right_size([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # 3
    print_result("Test 5", shift_right_size([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]))  # None


def test_is_perfect():
    print("\n--- Testing is_perfect ---")
    print_result("Test 1", is_perfect([2, 3, 2, 3, 0]))  # False
    print_result("Test 2", is_perfect([2, 3, 2, 1, 0]))  # False
    print_result("Test 3", is_perfect([]))               # True
    print_result("Test 4", is_perfect([1, 2, 3, 4, 0]))  # False
    try:
        is_perfect([2, 3, "a", 0])
    except TypeError as e:
        print_result("Test 5", f"Exception caught: {e}")  # Exception caught: ...


def test_identity_matrix():
    print("\n--- Testing identity_matrix ---")
    mat1 = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
    print_result("Test 1", identity_matrix(mat1))  # True

    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1.0]]
    try:
        identity_matrix(mat2)
    except TypeError as e:
        print_result("Test 2", f"Exception caught: {e}") # Exception caught: Not all values are int


def test_create_sub_matrix():
    print("\n--- Testing create_sub_matrix ---")
    mat = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [1, 0, 0, 0, 1]]
    print_result("Test 1", create_sub_matrix(mat, 3))  # 3x3 identity center

    mat_bad = [[1, 0], [0, 1, 0]]
    try:
        create_sub_matrix(mat_bad, 1)
    except IndexError as e:
        print_result("Test 2", f"Exception caught: {e}") # Exception caught: Not all rows are equal


def test_max_identity_matrix():
    print("\n--- Testing max_identity_matrix ---")
    mat1 = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1]]
    print_result("Test 1", max_identity_matrix(mat1))  # 3

    mat2 = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1.0]]
    print_result("Test 2", max_identity_matrix(mat2))   # Not all values are int
                                                        #Test 2: 0

    mat3 = [[1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1]]
    print_result("Test 3", max_identity_matrix(mat3))  # 1


if __name__ == "__main__":
    test_complement()
    test_shift_k_right()
    test_shift_right_size()
    test_is_perfect()
    test_identity_matrix()
    test_create_sub_matrix()
    test_max_identity_matrix()
