# My Approach using Merge Sort Algorithm
#
# Input:
# Left List: my_list = [3, 4, 6, 10, 11, 15]
# Right List: alices_list = [1, 5, 8, 12, 14, 19]
#
# Output:
# Merged List = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    sorted_list = []
    current_index_left = 0
    current_index_right = 0
    while len(sorted_list) < len(my_list) + len(alices_list):
        if ((current_index_left < len(my_list)) and
                (current_index_right == len(alices_list) or
                 my_list[current_index_left] < alices_list[current_index_right])):
            sorted_list.append(my_list[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(alices_list[current_index_right])
            current_index_right += 1
    return 


# Interview Cake Approach
 def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
    	# Case: my list is exhausted
        is_my_list_exhausted = current_index_mine >= len(my_list) 
        # Case: Alice's list is exhausted
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list