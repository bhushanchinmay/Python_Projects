# Input:
# unsorted_scores = [37, 89, 41, 65, 91, 53]
# HIGHEST_POSSIBLE_SCORE = 100
#
# Output:
# Returns [91, 89, 65, 53, 41, 37]
# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
##############################################################################################
# Solution:
# What if we did an in-order walk through score_counts.
# Each index represents a score and its value represents 
# the count of appearances. So we can simply add the score 
# to a new list sorted_scores as many times as count of appearances.
##############################################################################################
# Complexity:
# O(n) time and O(n)O(n) space, where nn is the number of scores.
############################################################################################## 
# Additional Information:
# Wait, aren't we nesting two loops towards the bottom? So shouldn't it be O(n^2)
# time? Notice what those loops iterate over. The outer loop runs once for each unique 
# number in the list. The inner loop runs once for each time that number occurred.

# So in essence we're just looping through the nn numbers from our input list, 
# except we're splitting it into two steps: (1) each unique number, and (2) each 
# time that number appeared.

# Here's another way to think about it: in each iteration of our two nested loops, 
# we append one item to sorted_scores. How many numbers end up in sorted_scores 
# in the end? Exactly how many were in our input list! nn.

# If we didn't treat highest_possible_score as a constant, we could call it k
# and say we have O(n+k) time and O(n+k) space.


def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores