import time

nums = [1,2,3,4,5,6,7,8,9,10]

# Example 1: Iteration vs Comprehension
print("Example 1 Iteration vs Comprehension")

squares = []
for n in nums:
        squares.append(n**2)

print(f"Iteration: {squares}")

squares = [n**2 for n in nums]

print(f"Comprehension: {squares}")

# Comprehension is 1.25 times faster 

# Example 2: Even Squares (Condition in a comprehension)
print("Example 2: Even Squares")

squares = []
for n in nums:
    if n % 2 == 0:
        squares.append(n**2)

print(f"Iteration: {squares}")

squares = [n**2 for n in nums if n % 2 == 0]

print(f"Comprehension: {squares}")
