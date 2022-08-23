# Readability in strings 

animal = "dog"
name = "Rover"
sound = "woof"

# How would you rank these in terms of readabiltiy? 
print("My name is " +name+ ", I am a " +animal+ " and I say "+sound+".")
print("My name is",name,", I am a",animal,"and I say",sound,".")
print("My name is {}, I am a {} and I say {}.".format(name, animal, sound))
print(f"My name is {name}, I am a {animal} and I say {sound}.")
