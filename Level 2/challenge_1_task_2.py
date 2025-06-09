# Test cases
test1 = 35231
test2 = 0
test3 = 23582357
test4 = 984764738
test5 = 45762893920
test6 = 548702838394

# Define function that reverses the number and puts it in a list format
def rev_list(test):
    result = []
    for num in str(test):
        result += [int(num)] 
    result = result[::-1]
    print(f'{test} becomes {result}')
    return result
    
#working through test cases
rev_list(test1)
rev_list(test2)
rev_list(test3)
rev_list(test4)
rev_list(test5)
rev_list(test6)
