print("--- Example 1 ---")

truth_check = 10 % 2 == 0 

if truth_check is True:
    print("True")

if truth_check == True:
    print("True")

if truth_check:
    print("True")

print("--- Example 2 ---")

full_list = [1, 2, 3, 4, 5]

if len(full_list) > 0:
    print("Full list")

if full_list: 
    print("Full list") 

print("--- Example 3 ---")

empty_list = []

if len(empty_list) == 0:
    print("Empty List")

if empty_list == []:
    print("Empty List")

if not empty_list:
    print("Empty List")

print("-----------------")


none_check = None

if none_check == None:
    print("!!!")