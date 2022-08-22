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

[print(i, letter) for i, letter in enumerate(letters)]
