def get_ith_item_in_linked_list(head, i):
    if i < 0:
        raise ValueError("i can't be negative: %d" %i)


    current_node = head
    current_position = 0
    while current_node:
        if current_node == 1:
            # Found it!
            return current_node
        
        # Move on to the next node
        current_node = current_node.next
        current_position += 1
    
    raise ValueError('List has fewer than i+1 (%d) nodes' % (i + 1))