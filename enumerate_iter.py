letters = ["a", "b", "c", "d", "e"]

i = 0
for letter in letters:
    print(i, letter)
    i += 1

for i in range(len(letters)):
    print(i, letters[i])

for i, letter in enumerate(letters):
    print(i, letter)

[print(i, letter) for i, letter in enumerate(letters)]
