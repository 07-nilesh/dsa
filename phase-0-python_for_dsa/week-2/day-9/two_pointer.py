# Two pointers — one of the most used patterns in DSA
# Use when: sorted array, searching pairs, palindromes

def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1       # need larger sum
        else:
            right -= 1      # need smaller sum
    return []
print(two_sum_sorted([2,7,11,15],9))