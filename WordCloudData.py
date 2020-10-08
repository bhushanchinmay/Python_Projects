# In our solution, we make three decisions:
#
# 1.  We use a class. This allows us to tie our methods together, calling them 
#   on instances of our class instead of passing references.
# 2. To handle duplicate words with different cases, we choose to make a word 
#   uppercase in our dictionary only if it is always uppercase in the original 
#   string. While this is a reasonable approach, it is imperfect (consider proper 
#   nouns that are also lowercase words, like "Bill" and "bill").
# 3. We build our own split_words() method instead of using a built-in one. This 
#   allows us to pass each word to our add_word_to_dictionary() method as it was split, 
#   and to split words and eliminate punctuation in one iteration.
#
# To split the words in the input string and populate a dictionary of the unique words to 
# the number of times they occurred, we:
#
# 1. Split words by spaces, em dashes, and ellipses—making sure to include hyphens surrounded 
#     by characters. We also include all apostrophes (which will handle contractions nicely 
#     but will break possessives into separate words).
# 2. Populate the words in our dictionary as they are identified, checking if the word is 
#     already in our dictionary in its current case or another case.
# 3. If the input word is uppercase and there's a lowercase version in the dictionary, 
#     we increment the lowercase version's count. If the input word is lowercase and there's 
#     an uppercase version in the dictionary, we "demote" the uppercase version by adding the 
#     lowercase version and giving it the uppercase version's count.
# 
# Runtime and memory cost are both O(n)O(n). This is the best we can do because we have to 
# look at every character in the input string and we have to return a dictionary of every 
# unique word. We optimized to only make one pass over our input and have only one O(n) data 
# structure.


class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):

            # If we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                        current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and \
                        input_string[i + 1].isalpha():
                    if current_word_length == 0:
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:
                            current_word_start_index + current_word_length]
                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0


    def add_word_to_dictionary(self, word):
        # If the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1