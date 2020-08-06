# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor

# numbers2 = list((1, 2, 3, 4, 5))

# get a value

print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list

fruits.remove('Grapes')

# insert into position 
fruits.insert(2, 'Strawberries')

# Remove with pop

fruits.pop(2)

# Reverse list

fruits.reverse()

print(fruits)