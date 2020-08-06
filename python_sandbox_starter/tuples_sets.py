# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
# fruit2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# get value
print(fruits[1])


# Can't change value
# fruits[0] = 'Pears'

# Delete tuple

del fruits2

# Get Length

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set 

fruits_set.add('Grape')

print(fruits_set)

# Remove from set

fruits_set.remove('Grape')

# Clear set

fruits_set.clear()



print(fruits_set)