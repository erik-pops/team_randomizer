import random

# Enter in the names of people playing
names = [
    'Popham',
    'Toni',
    'Spurlock',
    'Burton',
    'Bill',
    'Stine',
    'Krish',
    'Jalil',
    # 'Simpson',
    # 'Wasser',
    # 'Devon',
]

# choose how many people to pick for a team
team_size = 4

# ------------------------------------------------------------------------

# select 'k' items from 'population'
team = random.sample(population=names, k=team_size)
print("Team 1: ", team)
# determine 'difference' between all names and the random team
leftovers = list(set(names).difference(team))
print("Leftovers: ", leftovers)

