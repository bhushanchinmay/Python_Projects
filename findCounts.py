# Python3 program to print frequencies of all array 
# elements in O(1) extra space and O(n) time 

# Function to find counts of all elements present in 
# arr[0..n-1]. The array elements must be range from 
# 1 to n 
def findCounts(arr, n): 
	
	# Traverse all array elements 
	i = 0
	while i<n: 
		
		# If this element is already processed, 
		# then nothing to do 
		if arr[i] <= 0: 
			i += 1
			continue

		# Find index corresponding to this element 
		# For example, index for 5 is 4 
		elementIndex = arr[i] - 1

		# If the elementIndex has an element that is not 
		# processed yet, then first store that element 
		# to arr[i] so that we don't lose anything. 
		if arr[elementIndex] > 0: 
			arr[i] = arr[elementIndex] 

			# After storing arr[elementIndex], change it 
			# to store initial count of 'arr[i]' 
			arr[elementIndex] = -1
			
		else: 
			
			# If this is NOT first occurrence of arr[i], 
			# then decrement its count. 
			arr[elementIndex] -= 1

			# And initialize arr[i] as 0 means the element 
			# 'i+1' is not seen so far 
			arr[i] = 0
			i += 1

	print ("Below are counts of all elements") 
	for i in range(0,n): 
		print ("%d -> %d"%(i+1, abs(arr[i]))) 
	print ("") 


arr = [2, 3, 3, 2, 5] 
findCounts(arr, len(arr)) 

arr1 = [1] 
findCounts(arr1, len(arr1)) 

arr3 = [4, 4, 4, 4] 
findCounts(arr3, len(arr3)) 

arr2 = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1] 
findCounts(arr2, len(arr2)) 

arr4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3] 
findCounts(arr4, len(arr4)) 

arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
findCounts(arr5, len(arr5)) 

arr6 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
findCounts(arr6, len(arr6)) 
