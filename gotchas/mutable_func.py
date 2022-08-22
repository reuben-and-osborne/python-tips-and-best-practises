# BAD
# Mutable default values are defined when the function is
# Value will not reset when the function is called
def func(item, lst=[]):
    lst.append(item)
    return lst


print(func("A"))
print(func("B"))

# GOOD
# Assigning the mutable variable inside the function will solve the problem
def func(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(func("A"))
print(func("B"))
