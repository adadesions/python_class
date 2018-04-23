"""
    Create List for people in blood groups
    Groups -> A, B, O, AB
    in each group including people name
    
    for dataset,
        A -> 'arise', 'alice', 'auto'
        B -> 'Boron', 'Bertnard', 'Better'
        O -> 'Oreo', 'Otaro', 'Otus'

    Questions
        1. Print first person name for each groups
        2. Add 'Brown' to group B
        3. Add new AB group to list
        4. Copy all name in Group A, B to Group AB
        5. Delete all name in Group A
"""
# List

names_in_each_group = [    
# Group A [0]
    ['Arise', 'Alice', 'Auto'],

# Group B [1]
    ['Boron', 'Bernard', 'Better'],

# Group O [2]
    ['Orio', 'Otaro', 'Otsu']
# Group AB [3]
]
 # Part 1

print('First person name in all groups:', names_in_each_group [0][0], ',', names_in_each_group[1][0], ',', names_in_each_group[2][0])

# Part 2

names_in_each_group[1].append('Brown')
print('Group B plus one:', names_in_each_group[1])
 
# Part 3

names_in_each_group.append([])
print('Group AB set:', names_in_each_group[3])

# Part 4

names_in_each_group[3].append(names_in_each_group[0][0])
names_in_each_group[3].append(names_in_each_group[0][1])
names_in_each_group[3].append(names_in_each_group[0][2])
names_in_each_group[3].append(names_in_each_group[1][0])
names_in_each_group[3].append(names_in_each_group[1][1])
names_in_each_group[3].append(names_in_each_group[1][2])
names_in_each_group[3].append(names_in_each_group[1][3])
print('Name list in AB group:',names_in_each_group[3])

# Part 5

names_in_each_group[0].remove('Arise')
names_in_each_group[0].remove('Alice')
names_in_each_group[0].remove('Auto')
print('Groupe A was removed:', names_in_each_group[0])

# Final Part
for name_in_each_group in names_in_each_group:
    print('update the name in all groups:', name_in_each_group)
