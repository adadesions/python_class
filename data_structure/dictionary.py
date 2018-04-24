"""
 dict = {
     key1: value1,
     key2: value2,
 }
"""

# Create
fruit = {
    'apple': 10,
    'pine-apple': 12,
    'orange': 14,
}

# Access
print(fruit['apple'])

# Update and Edit
fruit['grape'] = 5
print(fruit)

fruit['apple'] = 9.5
print(fruit)

# Delete
del fruit['grape']
print(fruit)

# loop
for key, val in fruit.items():
    print('key:{}, val:{}'.format(key, val))

# loop 2
for key in fruit:
    print('key:{}, val:{}'.format(key, fruit[key]))
