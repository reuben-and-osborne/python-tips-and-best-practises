letters = ["a", "b", "c", "d", "e"]

# BAD
# No need to create counter variable
i = 0
for letter in letters:
    print(i, letter)
    i += 1

# BAD
# Easier to iterate over list items
for i in range(len(letters)):
    print(i, letters[i])


# GOOD
for i, letter in enumerate(letters):
    print(i, letter)


dct = {"a": 1, "b": 2, "c": 3}

# BAD
# Default is keys
for key in dct.keys():
    print(key, dct[key])

# BAD
# Better to iterate over the items
for key in dct:
    print(key, dct[key])

# GOOD
for key, value in dct.items():
    print(key, value)


letters = ["a", "b", "c", "d", "e"]

numbers = [1, 2, 3, 4, 5, 6]

# BAD
# Better to iterate over the items
for i in range(len(letters)):
    print(letters[i], numbers[i])

# BAD
# You can (should) iterate over both lists
for i, letter in enumerate(letters):
    print(letter, numbers[i])

# GOOD
for letter, number in zip(letters, numbers):
    print(letter, number)