# Write an efficient function that checks whether any permutation 
# of an input string is a palindrome.
#
# "civic" should return True
# "ivicc" should return True
# "civil" should return False
# "livci" should return False
# 
# use a set, adding and removing characters as we look through the
# input string, so the set always only holds the characters that appear
# an odd number of times.
#
# As we iterate through the characters in the input string:
# 1. If the character is not in unpaired_characters, we add it.
# 2. If the character is already in unpaired_characters, we remove it.
#
# Time Complexity: O(n)
#
# Space Complexity: O(1)
# Explanation: Our unpaired_characters set is the only thing taking
#   up non-constant space. We could say our space cost is O(n) as well, 
#   since the set of unique characters is less than or equal to nn. But we 
#   can also look at it this way: there are only so many different characters. 
#   How many? The ASCII character set has just 128 different characters (standard 
#   english letters and punctuation), while Unicode has 110,000 (supporting 
#   several languages and some icons/symbols). We might want to treat our number
#   of possible characters in our character set as another variable kk and say our
#   space complexity is O(k). Or we might want to just treat it as a constant, 
#   and say our space complexity is O(1).

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1