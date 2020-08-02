# Question: You've built an inflight entertainment system with on-demand movie streaming.
#
# Users on longer flights like to start a second movie right when their first one ends, 
# but they complain that the plane usually lands before they can see the ending. 
# 
# So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.
# 
# When building your function:
#
# 1. Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# 2. Optimize for runtime over memory
#
# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) 
# and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
#
# We make one pass through movie_lengths, treating each item as the first_movie_length. At each iteration, we:
#
# 1. See if there's a matching_second_movie_length we've seen already (stored in our movie_lengths_seen set) 
#    that is equal to flight_length - first_movie_length. If there is, we short-circuit and return True.
# 2. Keep our movie_lengths_seen set up to date by throwing in the current first_movie_length.
#
# Time Complexity: O(n); Space Complexity: O(n)


def can_two_movies_fill_flight(movie_lengths, flight_length):
	# Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False