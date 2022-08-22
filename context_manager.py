import json

# BAD
# If an exception is raised, file will never close
file = open("data/data.json")

data = json.load(file)

file.close()

print(data)

# GOOD
with open("data/data.json") as file:
    data = json.load(file)

print(data)
