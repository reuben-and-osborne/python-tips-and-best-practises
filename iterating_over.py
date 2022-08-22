# BAD
# Doesn't affect list
numbers = [1, 2, 3, 5, 6, 7, 0, 1]
for i, number in enumerate(numbers):
    if number < 5:
        del number

# Expected: numbers = [5, 6, 7]
print(numbers)

# BAD
# Deleting elements of a list whilst iterating over it
# Deleting items in this way changes the index of each element
numbers = [1, 2, 3, 5, 6, 7, 0, 1]
for i, number in enumerate(numbers):
    if number < 5:
        del numbers[i]

# Expected: numbers = [5, 6, 7]
print(numbers)

# GOOD
# Works but creates a new list
numbers = [1, 2, 3, 5, 6, 7, 0, 1]
numbers = [number for number in numbers if number >= 5]

print(numbers)

# Works but doesnt create new list
numbers = [1, 2, 3, 5, 6, 7, 0, 1]
numbers[:] = [number for number in numbers if number >= 5]

print(numbers)
