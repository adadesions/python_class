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

bloody_group = [
    # Group A [0]
    ['Arise', 'Alice', 'Auto'],

    # Group B [1]
    ['Boron', 'Bernard', 'Better'],

    # Group O [2]
    ['Orio', 'Otaro', 'Otsu']
    # Group AB [3]
]
group_name = ['A', 'B', 'O']
# Part 1

# print('First person name in all groups:',
#       bloody_group[0][0], ',',
#       bloody_group[1][0], ',',
#       bloody_group[2][0]
#       )
print('First person name in each groups: {0}, {1}, {2}'.format(
        bloody_group[0][0],
        bloody_group[1][0],
        bloody_group[2][0],
    )
)
for index, group in enumerate(bloody_group):
    for name in group:
        print('Group {0}: {1}'.format(group_name[index], name))
        break
# Part 2

bloody_group[1].append('Brown')
print('Group B plus one:', bloody_group[1])

# Part 3

bloody_group.append([])
print('Group AB set:', bloody_group[3])

# Part 4

# bloody_group[3].append(bloody_group[0][0])
# bloody_group[3].append(bloody_group[0][1])
# bloody_group[3].append(bloody_group[0][2])
# bloody_group[3].append(bloody_group[1][0])
# bloody_group[3].append(bloody_group[1][1])
# bloody_group[3].append(bloody_group[1][2])
# bloody_group[3].append(bloody_group[1][3])
# print('Name list in AB group:', bloody_group[3])

for i, group in enumerate(bloody_group):
    for name in group:
        if i > 1:
            break
        bloody_group[-1].append(name)

print('Name list in AB group:', bloody_group[3])

# Part 5

for names in bloody_group[0]:
    print(names)

print('Groupe A was removed:', bloody_group[0])

# Final Part
for name_in_each_group in bloody_group:
    print('update the name in all groups:', name_in_each_group)
