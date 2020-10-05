def pairs_count(arr, n, sum): 
    
    ans = 0

    arr = sorted(arr) 

    i, j = 0, n - 1

    dict = {}

    twice = 0

    for i in arr:
        if (i in dict): 
            dict[i] += 1
        else:
            dict[i] = 1


    for i in range(0, n):
        twice += dict[sum - arr[i]]

        if sum - arr[i] == arr[i]:
            twice -= 1

    return twice // 2

# Driver code 
arr = [1, 5, 7, 5, -1] 
n = len(arr) 
sum = 6

print(pairs_count(arr, n, sum)) 
