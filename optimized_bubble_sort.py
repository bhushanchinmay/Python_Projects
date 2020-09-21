# Consider the first pass through the outer loop. We’re making n-1 comparisons.
#
# We know the last value in the list is in its correct position, so we never need to consider it again. 
# The second time through the loop, we only need n-2 comparisons.
#
# As we correctly place more values, fewer elements need to be compared. An optimized version doesn’t 
# make n^2-n comparisons, it does (n-1) + (n-2) + ... + 2 + 1 comparisons, which can be simplified to (n^2-n) / 2 comparisons.
#
# This is fewer than n^2-n comparisons but the algorithm still has a big O runtime of O(N^2).

As the input, N, grows larger, the division by two has less significance. Big O considers inputs as they reach infinity so the higher order term N^2 completely dominates.

We can’t make Bubble Sort better than O(N^2), but let’s take a look at the optimized code and compare iterations between implementations!
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for el in arr:
    for index in range(len(arr) - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)

  print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
  print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))