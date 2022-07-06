type(3)
# <class 'int'>

# Turn things into ints
int(3.24)
# 3

# Turn things into floats
float(3)
# 3.0

# Turn things into bools
# All numbers are treated as true, except 0
bool(1)
# True

# All strings are treated as true, except the empty string ""
bool("asf")
# True

"Spam " * 4
# Spam Spam Spam Spam

# round(num,ndigits)
round(5.13567,2)
# 5.14

# ndigits=-1 rounds to the nearest 10
# ndigits=-2 rounds to the nearest 100, etc
# Useful for big numbers
round(76,-2)
# 100

# Print float
val = 19.211146
print(f"{val:.2f}")
# 19.21


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

# Print the biggest number and biggest modulo 5
print(max(100,51,14), max(100,51,14,key=mod_5),sep=' ')
# 100 14


def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False


def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog."""
    return (ketchup + mustard + onion) == 1


# Convert 07:05:45AM to 07:05:45 and 07:05:45PM to 19:05:45
def timeConversion(s):
    h = int(s[:2])
    msec = s[2:8]
    h = h % 12 if s[-2:] == 'AM' else h % 12 + 12
    return f"{h:02}{msec}"


animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))
#1: cat
#2: dog
#3: monkey   


# List
Lt = ['A', 'B', 'C', 'D']
Lt[0]
# 'A'
Lt[-1]
# 'D'
Lt[0:3] # = Lt[:3] # from index 0 to 2
# ['A', 'B', 'C']
Lt[2:] # from index 2 to end
# ['C', 'D']
Lt[1:-1] # all except the first and last
# ['B', 'C']
Lt[-3:] # the last 3
# ['B','C', 'D']

# LL is a list of lists
# LL[-1][1] gives the second from the last list

[1,2,3][1:]
#[2, 3]

Ls = ['C', 'B', 'A', 'D']
sorted(Ls) # sort in alphabetical order
# ['A', 'B', 'C', 'D']

Lt = ['A', 'B', 'C', 'D']
Lt.append('E') # add to the end
Lt
# ['A', 'B', 'C', 'D', 'E']
Lt.pop() # remove the last one
Lt
# ['A', 'B', 'C', 'D']
Lt.index('C') # find the index
# 2


# Tuples are almost same as lists, except
# 1) Tuples in () while Lists in []
# 2) Cannot be modified
t = (1, 2, 3)
# Tuples are often used for functions that have multiple return values.
x = 0.125
x.as_integer_ratio()
# (1, 8)
numerator, denominator = x.as_integer_ratio()
numerator, denominator
# 1 8


# Almost everything we can do to a list, we can also do to a string.
# Strings cannot be modified.
planet = 'Pluto'
planet[0]
# 'P'
planet[-3:]
# 'uto'
len(planet)
# 5
[char+'! ' for char in planet]
# ['P! ', 'l! ', 'u! ', 't! ', 'o! ']

planet = 'Pluto'
claim = "Pluto is a planet!"
claim.upper()
# 'PLUTO IS A PLANET!'
claim.lower()
# 'pluto is a planet!'
# Searching for the first index of a substring
claim.index('plan')
# 11
claim.startswith(planet)
# True
claim.endswith('planet')
# False
claim.endswith('planet!')
# True

words = claim.split()
words
# ['Pluto', 'is', 'a', 'planet!']

datestr = '1956-01-31'
year, month, day = datestr.split('-')
year,month,day
# 1956 01 31
'/'.join([month, day, year])
# '01/31/1956'
planet = 'Pluto'
print(planet + ', we miss you.')
# 'Pluto, we miss you.'

planet = 'Pluto'
position = 9
print("{}, you'll always be the {}th planet to me.".format(planet, position))
# "Pluto, you'll always be the 9th planet to me."

planet = 'Pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))


# List comprehension
squares = [n**2 for n in range(5)]
squares
# [0, 1, 4, 9, 16]

squares = []
for n in range(5):
    squares.append(n**2)
squares


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets
# ['Venus', 'Earth', 'Mars']

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets
# ['VENUS!', 'EARTH!', 'MARS!']


def count_negatives(nums):
    return len([num for num in nums if num < 0])

def count_negatives(nums):
    return sum([num < 0 for num in nums])


def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

print(elementwise_greater_than([1, 2, 3, 4], 2))
# [False, False, True, True]


# Dict
numbers = {'one':1, 'two':2, 'three':3}
numbers['one']
# 1
# add another key
numbers['eleven'] = 11
numbers
# {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}

for k in numbers:
    print("{} = {}".format(k, numbers[k]))
## one = 1
## two = 2
## three = 3
## eleven = 11
    
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial
## {'Mercury': 'M',
## 'Venus': 'V',
## 'Earth': 'E',
## 'Mars': 'M',
## 'Jupiter': 'J',
## 'Saturn': 'S',
## 'Uranus': 'U',
## 'Neptune': 'N'}

' '.join(sorted(planet_to_initial.keys()))
# 'Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus'
' '.join(sorted(planet_to_initial.values()))
# 'E J M M N S U V'

# dict.items() iterates over the keys and values of a dictionary simultaneously.
# an item refers to a key, value pair
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
##   Mercury begins with "M"
##     Venus begins with "V"
##     Earth begins with "E"
##      Mars begins with "M"
##   Jupiter begins with "J"
##    Saturn begins with "S"
##    Uranus begins with "U"
##   Neptune begins with "N"

# Create a dictionary with tuple keys
d = {(x, x + 1): x for x in range(10)}  
t = (5, 6)       # Create a tuple
print(d[t])
# 5    
print(d[(1, 2)])
# 1


def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.str.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices
