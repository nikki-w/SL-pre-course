# Code wars 1:

meet = {'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 
'saajid':2, 'alex':3, 'john':2, 'mr':0}

# Making note that 'mr' is the boss and doubling his happiness rating
meet['mr'] *= 2

# Collect everyones ratings
total_rating = 0
for rating in meet.values():
    total_rating += rating

# Determine what to do based off the average result
if total_rating/len(meet) <= 5:
    print('Get Out Now!')
else:
    print('Nice Work Champ!')


# Code wars 2:

# Test case that shows 'kill me now'
#staff = { "tim": "change", "jim": "accounts",
       # "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
       # "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
       # "mr": "finance" }

# Test case that shows 'i can handle this'
# staff = { "tim": "IS", "jim": "finance",
#       "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
#       "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
#       "alex": "regulation", "john": "accounts", "mr": "canteen" }

# Test case that shows 'party time!!'
staff = { 'tim': 'accounts', 'jim': 'accounts',
       'randy': 'pissing about', 'sandy': 'finance', 'andy': 'change',
       'katie': 'IS', 'laura': 'IS', 'saajid': 'canteen', 'alex': 'pissing about',
       'john': 'retail', 'mr': 'pissing about' }
  
# Loop to cycle through and assign boredom values to jobs  
sentiment_score = 0      
for value in staff.values():
    if value == 'accounts':
        sentiment_score += 1
    if value == 'finance':
        sentiment_score += 2
    if value == 'regulation':
        sentiment_score += 3
    if value == 'cleaning':
        sentiment_score += 4
    if value == 'retail':
        sentiment_score += 5
    if value == 'trading' or value == 'change':
        sentiment_score += 6
    if value == 'IS':
        sentiment_score += 8
    if value == 'canteen':
        sentiment_score += 10
    if value == 'pissing about':
        sentiment_score += 25

# Determine sentiment based on score        
if sentiment_score <= 80:
    print('kill me now')
elif 80 < sentiment_score < 100:
    print('i can handle this')
elif sentiment_score >= 100:
    print('party time!!')
