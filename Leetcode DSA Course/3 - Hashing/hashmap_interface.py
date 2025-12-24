# Declare a hash map
hash_map = {}

# Initialise with some key val pairs
hash_map = {1: 2, 5: 3, 7: 2}

# Checking if a key exists: use 'in' keyword
1 in hash_map # True
9 in hash_map # False

# Accessing a val given a key
hash_map[5] # 3

# Adding or updating a key
# If key already exists, value's updated
hash_map[5] = 6

# If key doesn't exist yet, key val. pair inserted
hash_map[9] = 15

# Deleting key: use del keyword, key must exist or
# you will get an error
del hash_map[9]

# Get size
len(hash_map) # 3

# Get keys: use .keys(). You can iterate over this 
# using for loop
keys = hash_map.keys()

for key in keys:
    print(key)

# Get values: use .values() (can also iterate over
# this with for loop)
values = hash_map.values()

for val in values:
    print(val)