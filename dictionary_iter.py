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
