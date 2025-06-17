# Create dictionaries for the people listed in the data table
Jane = {'First name':'Jane', 'Surname':'Doe', 'Age':42, 'Employed':'Yes'}
Tom = {'First name':'Tom', 'Surname':'Smith', 'Age':18, 'Employed':'Yes'}
Mariam = {'First name':'Mariam', 'Surname':'Coulter', 'Age':66, 'Employed':'No'}
Gregory = {'First name':'Gregory', 'Surname':'Tims', 'Age':8, 'Employed':'No'}

# Add them to a list called 'people'
people = [Jane, Tom, Mariam, Gregory]

# Loop over the dictionaries in the list, use the .get() command to extract info
# I made this into a function so the list can be printed in a more formatted way
def printing_list(people):
  for person in people:
      full_name = person.get('First name') + ' ' + person.get('Surname')
      age = person.get('Age')
      employed = person.get('Employed')

      print(f'Name: {full_name}')
      print(f'Age: {age}')
      print(f'Employed: {employed}')

# Funct that asks for users input on if they want to add or remove dictionaries
def input_funct():
    return input('Would you like to \'add\' or \'remove\'? ')

# Initial call of the add/remove decision
prompt = input_funct()

# While loop that breaks when the user enters anything but 'add' or 'remove'
while prompt.lower() == 'add' or prompt.lower() == 'remove':
  # Loop for if user adds
  if prompt.lower() == 'add':
    # Go through prompts
    user_name = input('What is your full name? ' )
    user_name = (user_name.title()).split()
    user_first_name = user_name[0]
    user_surname = user_name[1]
    user_age = input('What is your age? ')
    user_employed = input('Are you employed? ')
  
    # Add user input to 'people' list
    user = {'First name':user_first_name, 'Surname':user_surname, 'Age':int(user_age), 'Employed':user_employed.capitalize()}
    people.append(user)
    print('The updated list is...')
    printing_list(people)
    prompt = input_funct()
  # Loop for if user removes
  if prompt.lower() == 'remove':
    person_removed = input('What is the first name of the person you want to remove? ')
    for i in range(len(people) -1, -1, -1):
      # If first name matches the name that the user enters then it is popped out of the list
      if people[i].get('First name') == person_removed.title():
        people.pop(i)
        break
    print(f'The updated list is...')
    printing_list(people)
    prompt = input_funct()
