# Define test arrays from pre-work page
array1 = [2, 4, 1, 0, 2, -1]
array2 = [20, 50, 12, 6, 14, 8]
array3 = [100, -100]

# Create function to work out the min and max values in an array
def minmax(array):
    # Define starting point in array as 'base' min or max number
    min_val = array[0]
    max_val = array[0]
    
    # Check if next value in array is smaller than init, if it is then 
    # update the min value with the new min value
    for num in array:
        if num < min_val:
            min_val = num

    # Check if next value in array is smaller than init, if it is then
    # update the min value with the new min value
    for num in array:
        if num > max_val:
            max_val = num

    # Print vals
    vals = [min_val, max_val]
    print(vals)

# Test 1
minmax(array1)

# Test 2
minmax(array2)

# Test 3
minmax(array3)