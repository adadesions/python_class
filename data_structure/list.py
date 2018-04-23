"""
    List, structure, []
"""
# Create
fruits = ['apple', 'pine-apple', 'orange', 'grape']
print('Origin:', fruits)

# Read
print('Read index 0:', fruits[0])

# Insert
fruits.append('mango')
print('Updated', fruits)
# Update == Edit
fruits[0] = 'Avorgardo'
print('Edit:', fruits)

# Mixed Type
mixed = [1, 'a', 3.14, 'Ada']
print('Mixed:', mixed)

# Higher dimensional
seasons = [
    # Hot
    ['Thailand', 'India'],
    # Cold
    ['USA', 'Greenland']
]
print('Full Season', seasons)
print('Hot area', seasons[0][1])
print('All Cold area:', seasons[1])

# Accessed by loop
for fruit in fruits:
    print(fruit)

for countries in seasons:
    print(countries)
    for country in countries:
        print(country)

# Remove
fruits.remove('mango')
print('Remove', fruits)
