# mmn14_tester.py

from mmn14 import *

# ==================================
# Question 1: Test find_max
# ==================================
print("=== Question 1: find_max ===")

lst1 = [17, 40, 42, 2, 6, 11]
print(find_max(lst1))  # Expected: 42

lst2 = [5, 6, 7, 1, 2, 3, 4]
print(find_max(lst2))  # Expected: 7

lst3 = [2, 3, 4, 5, 6]
print(find_max(lst3))  # Expected: 6

lst4 = []
print(find_max(lst4))  # Expected: None


# ==================================
# Question 2: Test find_pairs
# ==================================
print("\n=== Question 2: find_pairs ===")

lst5 = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
print(find_pairs(lst5, 2))  # Expected: 4

print(find_pairs(lst5, 6))  # Expected: 2

print(find_pairs(lst5, 23))  # Expected: 0

lst6 = [1, 3, 5, 7, 9, 11]
print(find_pairs(lst6, 2))  # Expected: 5


# ==================================
# Question 3a: Test update_list
# ==================================
print("\n=== Question 3a: update_list ===")

lst7 = [3, 1, 8, 10, 6]
print(update_list(lst7, 1))  # Expected: [3, 8, 10, 6]

lst8 = [4, 3, 1, 3]
print(update_list(lst8, 3))  # Expected: [4, 1, 3]

lst9 = [3, 1, 8, 10, 6]
print(update_list(lst9, 2))  # Expected: [3, 1, 8, 10, 6]

lst10 = []
print(update_list(lst10, 5))  # Expected: []


# ==================================
# Question 3b: Test equal_lists
# ==================================
print("\n=== Question 3b: equal_lists ===")

lst11 = [1, 4, 3, 1, 2]
lst12 = [1, 1, 2, 3, 4]
print(equal_lists(lst11, lst12))  # Expected: True

lst13 = [8, 1, 3, 3]
lst14 = [8, 1, 3]
print(equal_lists(lst13, lst14))  # Expected: False

lst15 = [2, 2, 2]
lst16 = [2, 2, 2]
print(equal_lists(lst15, lst16))  # Expected: True

lst17 = [1, 2, 3]
lst18 = [3, 2, 2]
print(equal_lists(lst17, lst18))  # Expected: False

# ==================================
# Question 4: Test is_palindrome
# ==================================
print("\n=== Question 4: is_palindrome ===")

lst19 = ["abba", "readaer", "abba"]
print(is_palindrome(lst19))  # Expected: True

lst20 = ["abba"]
print(is_palindrome(lst20))  # Expected: True

lst21 = ["a", "aa", "aba", "a"]
print(is_palindrome(lst21))  # Expected: False

lst22 = []
print(is_palindrome(lst22))  # Expected: True

lst23 = ["raddar", "mom", "mom", "raddar"]
print(is_palindrome(lst23))  # Expected: True

