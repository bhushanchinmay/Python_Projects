def pairs_count(arr, n, sum): 
    
    # To store the count of pairs 
    ans = 0

    # Sort the given array 
    arr = sorted(arr) 

    # Take two pointers 
    i, j = 0, n - 1

    dict = {}

    for i in arr:
        if (i in dict): 
            dict[i] += 1
        else:
            dict[i] = 1

    twice = 0

    for i in range(0, n):
        twice += dict[sum - arr[i]]

        if sum - arr[i] == arr[i]:
            twice -= 1

    # Return the required answer 
    return twice // 2

# Driver code 
arr = [1, 5, 7, 5, -1] 
n = len(arr) 
sum = 6

print(pairs_count(arr, n, sum)) 

# This code is contributed by Mohit Kumar 
