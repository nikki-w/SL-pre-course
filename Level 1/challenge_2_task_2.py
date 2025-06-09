import random
import string

# Task 2:
first_name = input('Please enter your first name: ')

def reverse_name(first_name):
    """Function that reverses a name"""
    first_name_rev = first_name[::-1]
    return first_name_rev

re_name = reverse_name(first_name)
print(f'Your first name spelled backwards is {re_name}!')


surname = input('Please enter your surname: ')

def intersperse_name(first_name, surname):
    """Function that intersperses a first and surname together"""
    inter_name = ''
    length = min(len(first_name), len(surname))
    for i in range(length):
      inter_name += first_name[i] + surname[i]
    inter_name += first_name[length:] + surname[length:]
    return inter_name

inter_name = intersperse_name(first_name, surname)
print(f'Your first and second names interspersed is {inter_name}!')

def format_name(inter_name):
  """Function that splits a string into two and formats each half as if it is a full name"""
  form_first_name = inter_name[:len(inter_name)//2 + len(inter_name)%2]
  form_surname = inter_name[len(inter_name)//2 + len(inter_name)%2:]
  form_name = (form_first_name + ' ' + form_surname).title()
  return form_name

form_name = format_name(inter_name)
print(f'Your formatted interspersed name is {form_name}!')

# Task 3:
print('Welcome to the username creator, please choose one of the following options:')
opt = input('\'Option 1\': Create a username based on a name or \'Option 2\': Generate a random username ').capitalize()
if opt == 'Option 1' or opt == '1':
  first = input('Enter your first name here: ')
  sur = input('Enter your surname here: ')
  int_name = intersperse_name(first, sur)
  username = format_name(int_name)
  print(f'Your username is: {username}')
elif opt == 'Option 2' or opt == '2':
  length = input('Enter the length you want your username to be: ')
  username = ''
  for i in range(int(length)):
    username += (''.join(random.choice(string.ascii_uppercase + string.digits))).lower()
    i += 1
  print(f'Your username is: {username}')
else:
  print('Oops! That isn\'t a recognised option, please enter either \'Option 1\' or \'Option 2\'')
