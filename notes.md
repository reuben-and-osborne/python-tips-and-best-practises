# Python Tips, Tricks and Best Practises

A look into some python tips, tricks and best practises with a focus on readability. 

## Tips and tricks...

### 01. Conditions

#### Boolean 
---

#### input:
```
truth_check = True
```
---
```
if truth_check is True:
    print("Pass")
```
#### output:
```
Pass
```
---
```
if truth_check == True:
    print("True")
```
#### output:
```
Pass
```
---
```
if truth_check:
    print("True")
```
#### output:
```
Pass
```

- The third example uses a method called **Truth Value Testing**. 
---

#### Empty List
---
#### input
```
empty_list = []
```
---
```
if len(empty_list) == 0:
    print("Empty List")
```
#### output:
```
Empty List
```
---
```
if empty_list == []:
    print("Empty List")
```
#### output:
```
Empty List
```
---
```
if not empty_list:
    print("Empty List")
```
#### output:
```
Empty List
```

- Truth Value testing essentially means we are testing against the lists boolean value.
- This is possible because, in Python empty sequences are considered to be false.
- So as `empty_list` is empty it is valued as false. Thus meaning we need a `not` to trigger the conditional to test for an empty list.
  
---

### 02. Sets
Sets are like tuples and lists, they are a standard data type that allow you to store data. 
The difference between lists and sets, sets cannot have multiple occurrences of the same element.

#### input: 
```
example_list = [1,1,2,1,3,3,2,4]
example_set = {1,1,2,1,3,3,2,4}
```
```
print(f"List: {example_list}")
print(f"Set: {example_set}")
```
output:
```
List: [1, 1, 2, 1, 3, 3, 2, 4]
Set: {1, 2, 3, 4}
```
---
#### Use case: Remove duplicate values from a list (begineer level coding challenage)
Example 1: iteration

```
output = []
for num in example_list:
    if num not in output:
        output.append(num)
print(f"Iteration: {output}")
```
output:
```
Iteration: [1,2,3,4]
```

Example 2: Use set
```
output = list(set(example_list))
print(f"Set: {output}")
```

output:
```
Set: [1,2,3,4]
```
---
- Using a set is around 2 times faster 
- It is also less lines of code
- And easier to read

### 03. List Comprehensions
Lets consider this problem:
Square the numbers the in the list `nums`

input:
```
nums = [1,2,3,4,5,6,7,8,9,10]
```

#### Example 1: Iteration vs Comprehension

```
squares = []
for n in nums:
        squares.append(n**2)
print(f"Iteration: {squares}")
```
output:
```
Iteration: [1,4,9,16,25,36,49,64,81,100]
```
```
squares = [n**2 for n in nums]
print(f"Comprehension: {squares}")
```
output:
```
Comprehension: [1,4,9,16,25,36,49,64,81,100]
```
- Comprehension is 1.25 times faster 
- But again we have a much cleaner 1 line solution.

---
#### Example 2: Even Squares
We could also add a condition into the comprehension. 

Lets only square the even numbers in `nums`

```
squares = []
for n in nums:
    if n % 2 == 0:
        squares.append(n**2)
print(f"Iteration: {squares}")
```
output:
```
Iteration: [4, 16, 36, 64, 100]
```
```
squares = [n**2 for n in nums if n % 2 == 0]
print(f"Comprehension: {squares}")
```
output:
```
Comprehension: [4, 16, 36, 64, 100]
```
- cleaner code overall
- I tend not to make my list comprehensions any more complex than this as readability starts to decrease.
- 
---
### 04. Splicing Syntax
Splicing lists and strings is a useful tool. 
The syntax is `L[start:end:step]`
Consider list `L`
input:
```
L = [i for i in range(10)]
```

First 5 items:
```
>>> print(L[:5])
[0, 1, 2, 3, 4]
```

Last 5 items:
```
>>> print(L[5:])
[5, 6, 7, 8, 9]
```

Items 4,5,6
```
>>> print(L[4:7])
[4, 5, 6]
```

Every other item
```
>>> print(L[::2])
[0, 2, 4, 6, 8]
```

Reverse the list
```
>>> print(L[::-1])
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

---

### 05. Iteration Syntax
How can we iterate over the list and print each letter and it's index? 

input:
```
letters = ["a", "b", "c", "d", "e"]
```

Bad Example
- No need to create counter variable.
```
i = 0
for letter in letters:
    print(i, letter)
    i += 1
```
output:
```
0 a
1 b
2 c
3 d
4 e
```

Bad Example 2
- We could use range and len to count up in i.
- This hinders readability.
```
for i in range(len(letters)):
    print(i, letters[i])
```
output:
```
0 a
1 b
2 c
3 d
4 e
```

Better example:
- Enumerate lets us iterate over the items and keeps track of our index value.
```
for i, letter in enumerate(letters):
    print(i, letter)
```
output:
```
0 a
1 b
2 c
3 d
4 e
```
- enuerate is faster when you want to access both index and letter
- However slower if you just wanted to cycle through the index. 
  
### 06. String Format
Let's look at the readability in formatted strings.

input:
```
animal = "dog"
name = "Rover"
sound = "woof"
```
Which one below is the most readable? 
```
print("My name is " +name+ ", I am a " +animal+ " and I say "+sound+".")
print("My name is",name,", I am a",animal,"and I say",sound,".")
print("My name is {}, I am a {} and I say {}.".format(name, animal, sound))
print(f"My name is {name}, I am a {animal} and I say {sound}.")
```
output:
```
My name is Rover, I am a dog and I say woof.
My name is Rover , I am a dog and I say woof .
My name is Rover, I am a dog and I say woof.
My name is Rover, I am a dog and I say woof.
```
You can see I struggled with the spacing of example 2. For me 1 and 4 are the most readable.

You can also embed expressions, which is evaluated at run time: 

```
>>> print(f"10 divded by 2 is {10/2}")
5.0
```

---
## Some things to avoid...

### 08. Context Manager

data.json:
```
{
    "Hello": "World"
}
```

Lets compare these:
1:
```
file = open("data.json")
data = json.load(file)
...
file.close()
```
2:
```
with open("data.json") as file:
    data = json.load(file)
...
```
The issue here is in example one there is a possibility that the file may never close. E.g if an expection occurs... 
Example 2 is equivalent to writing:
```
file = open('data.json', 'w')
try:
    data = json.load(file)
finally:
    file.close()
```
---
## Style 

A little bit on style...

### 10a. PEP8
[PEP8](https://peps.python.org/pep-0008/)

- PEP stands for Python Enhancement Proposal 
- PEP8 is a document that provides guidelines and best practices on how to write Python code.
- Aims to improve readability and consistency of Python code.

[RealPython Blog on PEP8](https://realpython.com/python-pep8/)

### 10b. Google Style Guide
The Google Python Style Guide is a list of dos and donts for Python programmers at google. 
It follows PEP8 and has good sections on docstrings.

[Google Styling Guide For Python](https://google.github.io/styleguide/pyguide.html)

[Docstrings ](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)


### 10c. Naming Convension
[Google's Naming](https://google.github.io/styleguide/pyguide.html#316-naming)

1. Modules:
```
name_of_module.py
```
2. Classes
```
NameOfClass()
```
3. Functions
```
def name_of_function(x):
```
4. Variables 
```
name_of_variable = 123
```

### 10d. Type Hint
Example:
```
def func(a):
```
vs
```
def func(a: int) -> list[int]:
```
benefits of type hints:
1. less documentation (everyone hates writing docs)
2. live errors in your ide 
3. enforces you to be explict about your data structures (Type-DD)
4. simplifiy your code (less if statements to check types etc.)


