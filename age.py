# Code that asks a user to input a date and return the age between the current
# date and the given date
import datetime
#from dateutil import relativedelta

# Create function that allows user to input a date and it will return the current
# age of that year from todays date
def date_age():
    # Ask user for their date in a specific format
    user_date = input('Please enter a date in the format YYYY-MM-DD (including the hyphens)')

    # user strptime to extract the YYY MM and DD from the users input so it 
    # follows the formatting requirements of the datetime module
    user_date = datetime.datetime.strptime(user_date, '%Y-%m-%d')
    #print(user_date.year)
    # Use datetime to get current date
    current_date = datetime.datetime.today()

    # Calculate the difference which returns the days from the users input to 
    # todays date and, from that, calculate the number of years its been
    diff = current_date.year - user_date.year
    if current_date.month < user_date.month or (current_date.month == user_date.month and current_date.day < user_date.day):
        diff -= 1
    print(f'Years between your inputted date and the current date is: {diff}')

# Check it works using the two suggested dates on the pre-work page
date_age()

