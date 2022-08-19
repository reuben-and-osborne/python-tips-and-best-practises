nums = [1,2,3,4,5,6,7,8,9,10]

squares = []
for n in nums:
        squares.append(n**2)
print(squares)

squares = [n**2 for n in nums]
print(squares)

# squares = []
# for n in nums:
#     if n % 2 == 0:
#         squares.append(n**2)
# print(squares)

# squares = [n**2 for n in nums if n % 2 == 0]
# print(squares)
