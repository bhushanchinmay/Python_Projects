# define binary_search()
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx+1:]
    # make a variable: result and assign it to a recursive call of binary_search() given right_half and target.
    # Why are we storing this in a variable?
    #
    # We’re making a smaller copy of the sorted list at each recursive call, so our indices for the same values change:
    #
    # sorted_list = [7, 8, 9, 10, 11]
    # right_half = [10, 11]
    #
    # # index of "11" in sorted_list: 4
    # # index of "11" in right_half: 1
    # We can account for the missing indices by returning the result plus the index segments of the lists we’ve discarded.
    #
    # We’ll do this in the form of mid_idx + 1.
    # sorted_list = [7, 8, 9, 10, 11]
    # binary_search(sorted_list, 11)
    # mid_idx = 2
    # # 9 < 11, we search in right half...
    # # within the recursive call:
    # # right_half = [10, 11]
    # # mid_idx = 1
    # # target matched, we return 1
    # # within original call, result is 1
    # (result + mid_idx + 1) == 4
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1
# For testing:
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 16))