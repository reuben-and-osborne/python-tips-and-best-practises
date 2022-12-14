import time

example_list = [1,1,2,1,3,3,2,4]
example_set = {1,1,2,1,3,3,2,4}

print(f"List: {example_list}")
print(f"Set: {example_set}")

print("--- Use case ---")
# Use case: Remove duplicate values from a list
# Example 1: iteration

output = []
for num in example_list:
    if num not in output:
        output.append(num)

print(f"Iteration: {output}")

# Example 2: Use set
output = set(example_list)
print(f"Set: {output}")

# Example 2 is about 2 times faster 