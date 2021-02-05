arr = [0,1,4,2,0,0,0,5,0,13,7,0,8,9,0,0,5,7]
start = 0
n = len(arr)
count = 0 # Count of non-zero elements 
      
    # Traverse the array. If element  
    # encountered is non-zero, then 
    # replace the element at index 
    # 'count' with this element 
for i in range(n): 
    if arr[i] != 0: 
          
        # here count is incremented 
        arr[count] = arr[i] 
        count+=1
  
# Now all non-zero elements have been 
# shifted to front and 'count' is set 
# as index of first 0. Make all  
# elements 0 from count to end. 
while count < n: 
    arr[count] = 0
    count += 1
print(arr)
