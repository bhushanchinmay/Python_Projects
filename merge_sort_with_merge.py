def merge_sort(items):
  # base case
  if len(items) <= 1:
    return items

  # splitting the unordered list
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  # merging the sorted sub-list
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  # checking whether left and right sub-list has elements
  while (left and right):

    # comparing the first left and first right element in the left and right sub list
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  # adding left over elements to the result list
  if left:
    result += left
  if right:
    result += right

  return result


# testing out the our function
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
