import time

nums = [1,2,3,4,5,6,7,8,9,10]

# Example 1: Iteration
start = time.perf_counter()

squares = []
for n in nums:
        squares.append(n**2)

end = time.perf_counter()
print(f"{squares} in {(end-start)*1000}")
ex1_time = end-start

# Example 2: Comprehension
start = time.perf_counter()

squares = [n**2 for n in nums]

end = time.perf_counter()
print(f"{squares} in {(end-start)*1000}")
ex2_time = end-start

print(f"{round(ex1_time/ex2_time, 2)} times faster")

# Example 3: Even Squares

# squares = []
# for n in nums:
#     if n % 2 == 0:
#         squares.append(n**2)
# print(squares)

# squares = [n**2 for n in nums if n % 2 == 0]
# print(squares)
