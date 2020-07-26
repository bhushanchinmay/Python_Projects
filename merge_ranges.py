# Input :   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# 
# Output :   [(0, 1), (3, 8), (9, 12)]
# 
# Write a function merge_ranges() that takes a list of multiple
# meeting time ranges and returns a list of condensed ranges.
# 
# Do not assume the meetings are in order. 
# 
# The meeting times are coming from multiple teams.
# 
# 
# 
# Solution : First, we sort our input list of meetings by start time so any meetings 
# that might need to be merged are now next to each other.
#
# Then we walk through our sorted meetings from left to right. At each step, either:
#
#   1. We can merge the current meeting with the previous one, so we do.
#   2. We can't merge the current meeting with the previous one, so we know the previous meeting 
#      can't be merged with any future meetings and we throw the current meeting into merged_meetings.
#
#
# Complexity
# O(nlgn) time and O(n) space.
#
# Even though we only walk through our list of meetings once to merge them, we sort all the meetings first, 
# giving us a runtime of O(nlgn). It's worth noting that if our input were sorted, we could skip the sort and do this in O(n) time!
#
# We create a new list of merged meeting times. In the worst case, none of the meetings overlap, giving us a list 
# identical to the input list. Thus we have a worst-case space cost of O(n).


def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings