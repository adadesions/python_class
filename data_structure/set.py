"""
    Set == Mathematical Set
    set = {}
"""

fruit = {'apple', 'apple', 'orange
print(fruit)

# Fast check
print('is apple:', 'apple' in fruit)

a = {1, 2, 3}
b = {0, 1}

# Difference
print('Diffence a-b =', a-b)

# Union
print('a Union b =', a | b)

# Intersection
print('a intersect b =', a & b)

# Not in both
print('In a and b but not both = ', a ^ b)