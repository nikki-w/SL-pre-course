# Test cases
test1 = [118,117,120]
test2 = [101,121,110,113,113,103]
test3 = [118,103,110,109,104,106]
test4 = [107,99,110,107,118,106,112,102]
test5 = [100,100,116,105,117,121 ]

# Create function to convert number (key) into ascii (value) and add it to
# a list that contains the output
def num_obj(test):
  output = []
  for num in test:
    key = str(num)
    value = chr(num)
    output.append({key : value})
  return output

# Print the test cases
print(f'Test case 1: {num_obj(test1)}')
print(f'Test case 2: {num_obj(test2)}')
print(f'Test case 3: {num_obj(test3)}')
print(f'Test case 4: {num_obj(test4)}')
print(f'Test case 5: {num_obj(test5)}')
