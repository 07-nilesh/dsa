# --- Snippet A ---
def process_data(nums):
    n = len(nums)
    for i in range(n): #O(n)
        print(nums[i])
    for j in range(n):  #O(n)
        print(nums[j])
"""
TC: O(n)
space: O(1)
"""
# --- Snippet B ---
def grid_walk(n):
    for i in range(n):
        for j in range(50):
            print(i, j)
"""
TC: O(n^2)
space: O(1)
"""

# --- Snippet C ---
def clone_and_check(nums):
    new_list = []
    for num in nums:
        new_list.append(num)
    return nums[0] in new_list
"""
TC: O(n)
space: O(n)
"""
# --- Snippet D ---
def lookup_squares(n):
    squares_dict = {}
    for i in range(n):
        squares_dict[i] = i * i
    return squares_dict
"""
TC: O(n)
space: O(n)
"""
# --- Snippet E ---
def staggered_loops(nums):
    n = len(nums)
    for i in range(n):
        print(nums[i])
        
    for j in range(n):
        for k in range(10):
            print(nums[j], k)
"""
TC: O(n)
space: O(1)
"""
# --- Snippet F ---
def data_cleanup(matrix):
    # matrix is an n x n 2D list
    n = len(matrix)
    first_row_sum = 0
    for j in range(n):
        first_row_sum += matrix[0][j]
    return first_row_sum
"""
TC: O(n)
space: O(1)
"""
# --- Snippet G ---
def dynamic_halving(n):
    count = 0
    current_value = n
    while current_value > 1:
        current_value = current_value // 2
        count += 1
    return count
"""
TC: O(logn)
space: O(1)
"""
# --- Snippet H ---
def double_trouble_branch(n):
    if n <= 1:
        return 1
    # Note: Look at how many recursive paths branch out from this single frame!
    left_path = double_trouble_branch(n - 1)
    right_path = double_trouble_branch(n - 1)
    return left_path + right_path
"""
TC: O(2^n)
space: O(1)
"""
# --- Snippet I ---
def standard_library_magic(nums):
    # This invokes Timsort under the hood on a list of size n
    nums.sort()
    
    # After sorting, we execute one flat loop across the elements
    for item in nums:
        print(item)
"""
TC: O(nlogn)
space: O(1)
"""