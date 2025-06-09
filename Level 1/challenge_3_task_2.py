# Programme for summing numbers between 0 and a user-specified number
def sum_funct():
  num = ask_user_for_number()
  list_num = list(range(int(num)+1))
  total = sum(list_num)
  print(f'The sum of numbers 0 to {num} is: {total}')


# Programme for summing numbers that are multiples of 3 or 5 
# between 0 and a user-specified number
def multiple_sum():
  num = ask_user_for_number()
  num_list = list(range(1, int(num)+1))
  i = 0
  j = 0
  total = 0
  for i in range(0, len(num_list)):
    if num_list[i]%3 == 0 or num_list[i]%5 == 0:
      total += num_list[i]
      i += 1
    else:
      i += 1
  print(f'The sum of numbers divisible by 3 or 5 from 1 to {num} is: {total}')


# Programme that asks user for input number and gives option to choose between
# computimg the sum or computing the product or 1, .., n
def input_options():
  num = ask_user_for_number()
  option = input('Now select if you would like to either 1. Compute the sum of this number or 2. Compute the product: ')
  if option == '1' or option == '1.' or option.capitalize() == 'Option 1' or option.capitalize() == 'Option 1.':
    print(f'You have selected to calculate the sum of {num}')
    list_num = list(range(int(num)+1))
    total = sum(list_num)
    print(f'The sum of numbers 0 to {num} is: {total}')
  elif option == '2' or option == '2.' or option.capitalize() == 'Option 2' or option.capitalize() == 'Option 2.':
    print(f'You have selected to calculate the product of {num}')
    list_num = list(range(1, int(num)+1))
    answer = 1
    for i in range(len(list_num)):
      answer *= int(list_num[i])
    print(f'Your answer is {answer}')
  else:
    print('Oops! That doesn\'t appear to be the correct input, please try again')

# Programme for asking users to input a number, while verifying a valid number is entered
def ask_user_for_number():
  num = input('Please choose a number: ')
  if num.isdigit():
    return num
  elif num == '' or num == ' ':
      print('Oops! There doesn\'t appear to be any input, please try again')
  else:
    print('Oops! That doesn\'t appear to be a number, please try again')


# Check to make sure everything works as expected
sum_funct()
multiple_sum()
input_options()
