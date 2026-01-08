# Declaration.
hash_map = {}

# Can initialize with some key val. pairs.
hash_map = {1: 2, 5: 3, 7: 2}

# Checking if key exists: use "in" keyword.
1 in hash_map # True.
9 in hash_map # False.

# Accessing a value given a key.
hash_map[5] # 3.

# Adding or updating a key.
# If key already exists, val. updated.
hash_map[5] = 6

# If key doesn't exist yet, key val. pair inserted.
hash_map[9] = 15

# Deleting a key uses del keyword. Key must exist
# or you'll get an error.
del hash_map[9]

# Get size.
len(hash_map) # 3

# Get keys: using .keys(), you can iterate over
# this using a for loop.
keys = hash_map.keys()
for key in keys:
    print(key)

# Get vals.: use .values().
values = hash_map.values()
for val in values:
    print(val)