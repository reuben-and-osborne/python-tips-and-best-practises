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
