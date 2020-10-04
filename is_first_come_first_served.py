# The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
#
# The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
#
# Each customer order (from either register) as it was finished by the kitchen. (served_orders)
#
# Take Out Orders: [1, 3, 5]
# Dine In Orders: [2, 4, 6]
# Served Orders: [1, 2, 4, 6, 5, 3] 
# 
# Complexity:
# O(n) time and O(1)O(1) additional space.
#
# Solution:
#
# We walk through served_orders, seeing if each customer order so far matches a customer order from one of the two registers. To check this, we:
#
# 1. Keep pointers to the current index in take_out_orders, dine_in_orders, and served_orders.
# 2. Walk through served_orders from beginning to end.
# 3. If the current order in served_orders is the same as the current customer order in take_out_orders, 
#       increment take_out_orders_index and keep going. This can be thought of as "checking off" the current customer order 
#       in take_out_orders and served_orders, reducing the problem to the remaining customer orders in the lists.
# 4. Same as above with dine_in_orders.
# 5. If the current order isn't the same as the customer order at the front of take_out_orders or dine_in_orders, 
#       we know something's gone wrong and we're not serving food first-come, first-served.
# 6. If we make it all the way to the end of served_orders, we'll check that we've reached the end of take_out_orders 
#       and dine_in_orders. If every customer order checks out, that means we're serving food first-come, first-served.


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True