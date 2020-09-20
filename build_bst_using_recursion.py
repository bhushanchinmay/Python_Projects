# We assume our function will receive a sorted list of values as input.
#
# This is necessary to construct the binary search tree because we’ll be relying on the ordering of the list input.
#
# Our high-level strategy before moving through the checkpoints.
#
# base case: the input list is empty
# Return "No Child" to represent the lack of node
# 
# recursive step: the input list must be divided into two halves
#   Find the middle index of the list
#   Store the value located at the middle index
#   Make a tree node with a "data" key set to the value
#   Assign tree node’s "left child" to a recursive call using the left half of the list
#   Assign tree node’s "right child" to a recursive call using the right half of the list
# Return the tree node

def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"

  middle_index = len(my_list) // 2
  middle_value = my_list[middle_index]
  
  print("Middle index: {0}".format(middle_index))
  print("Middle value: {0}".format(middle_value))
  
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[ : middle_index])
  tree_node["right_child"] = build_bst(my_list[middle_index + 1 : ])

  return tree_node
  
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"