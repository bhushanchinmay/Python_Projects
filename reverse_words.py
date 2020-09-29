# Ques. Write a function reverse_words() that takes a message as a list of characters 
# and reverses the order of the words in place
#
# Ans.
# 1. Reverse all the characters in the entire message, giving us 
#    the correct word order but with each word backward.
# 2. Reverse the characters in each individual word.
#
# Input: the eagle has landed
#  [ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
#  'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ]

# Character-reversed: dednal sah elgae eht
#  [ 'd', 'e', 'd', 'n', 'a', 'l', ' ', 's', 'a', 'h', ' ',
#  'e', 'l', 'g', 'a', 'e', ' ', 'e', 'h', 't' ]

# Word-reversed (desired output): landed has eagle the
#  [ 'l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ',
#  'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e' ]
#
# Time Complexity: O(n)
#
# Space Complexity: O(1); Since in-place.
#
# Note: The naive solution of reversing the words one at a time had a worst-case O(n^2) runtime. 
# That's because swapping words with different lengths required "scooting over" all the other characters to make room.
#
# To get around this "scooting over" issue, we reversed all the characters in the message first. 
# This put all the words in the correct spots, but with the characters in each word backward. 
# So to get the final answer, we reversed the characters in each word. This all takes two passes 
# through the message, so O(n) time total.
#
# This might seem like a blind insight, but we derived it by using a clear strategy:
#
# Solve a simpler version of the problem (in this case, reversing the characters instead 
# of the words), and see if that gets us closer to a solution for the original problem.


def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1