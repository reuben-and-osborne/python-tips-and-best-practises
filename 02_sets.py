import time

example_list = [1,1,2,1,3,3,2,4]
example_set = {1,1,2,1,3,3,2,4}

print(f"List: {example_list}")
print(f"Set: {example_set}")

# Use case: Remove duplicate values from a list
# Example 1: iteration
start = time.perf_counter()

output = []
for num in example_list:
    if num not in output:
        output.append(num)

end = time.perf_counter()
print(f"Using iteration: {output} in {(end-start)*1000}")
ex1_time = end-start

# Example 2: Use set
start = time.perf_counter()

output = set(example_list)

end = time.perf_counter()
print(f"Using set: {output} in {(end-start)*1000}")
ex2_time = end-start

print(f"{round(ex1_time/ex2_time, 3)} times faster")