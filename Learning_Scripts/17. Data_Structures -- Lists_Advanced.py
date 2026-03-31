# ╔══════════════════════════════════════════════════════════╗
# ║             📑  INDEX — Lists Fundamentals              ║
# ╠══════════════════════════════════════════════════════════╣
# ║  📋  SECTION 1 — Copy                                   ║
# ║      ⚠️  Assignment  →  same object, risky              ║
# ║      🪞  Shallow     →  independent, top-level only     ║
# ║      🔬  Deep        →  fully independent, all levels   ║
# ║      🔍  is Operator →  checks if same object in memory ║
# ╠══════════════════════════════════════════════════════════╣
# ║  🔗  SECTION 2 — Combining Lists                        ║
# ║      ➕  +           →  creates a new combined list      ║
# ║      🔁  .extend()   →  expands original list in place  ║
# ║      🤐  zip()       →  pairs items by position         ║
# ╠══════════════════════════════════════════════════════════╣
# ║  🔄  SECTION 3 — Iterators & Iterables                  ║
# ║      🔢  enumerate() →  adds index counter to each item ║
# ║      🔃  reversed()  →  loops backwards, safe           ║
# ║      🤐  zip()       →  pairs items while looping       ║
# ║      🗺️  map()       →  transforms every item           ║
# ╠══════════════════════════════════════════════════════════╣
# ║  🚦  SECTION 4 — Filter                                 ║
# ║      🚦  filter()    →  keeps only items that pass      ║
# ║      🔤  str.isalpha →  keeps only alphabetic items     ║
# ╚══════════════════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════╗
# ║  📋  SECTION 1 — Copy                                   ║
# ╚══════════════════════════════════════════════════════════╝

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ⚠️ Assignment Copy ( = )
# This actually references the same list — does NOT create a new copy
# Both variables point to the SAME object in memory
# Any change on one WILL affect the other — very risky!
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

letters = ['a', 'b', 'c']
letters_copy = letters          # ⚠️ Not a real copy — both point to the same list in memory
letters.pop()                   # 🗑️ Removes last item from 'letters' — affects letters_copy too!
letters_copy.append('z')        # ➕ Appends to letters_copy — affects letters too!

print(f"Original : {letters} \nCopy : {letters_copy}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 🪞 Shallow Copy ( .copy() )
# Creates an independent copy at the TOP level only
# Modifying the copy will NOT affect the original — for flat (non-nested) lists
# ⚠️ BUT for nested lists, inner lists are still shared (see matrix example below)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

letters = ['a', 'b', 'c']
letters_copy = letters.copy()   # 🪞 Real independent copy — changes won't cross over
letters.pop()                   # 🗑️ Only affects 'letters'
letters_copy.append('z')        # ➕ Only affects 'letters_copy'

print(f"Original : {letters} \nCopy : {letters_copy}")

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix_copy = matrix.copy()
matrix.pop()                        # 🗑️ Removes Row 2 — only affects original (top-level change)
matrix_copy[0].append('z')          # ⚠️ Only Top Level Is Copied, And Deep Level Is Shared, Hence Any Update On Copy Would Reflect On Original On This Scenario 

print(f"Original : {matrix} \nCopy : {matrix_copy}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# 🔬 Deep Copy ( copy.deepcopy() )
# Creates a fully independent copy — ALL levels (including nested lists) are duplicated
# Changes to the copy will NEVER affect the original, no matter how deep
# Use this whenever you're working with nested / matrix lists
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

import copy
matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix_copy = copy.deepcopy(matrix)    # 🔬 Fully independent — even inner lists are new objects
matrix.pop()                           # 🗑️ Only affects original
matrix_copy[0].append('z')             # ➕ Only affects copy — original is safe ✅

print(matrix)
print(matrix_copy)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 🔍 IS OPERATOR
# Checks If Two Variables Refer to the Same Object
# == checks if values are equal | is checks if they're the SAME object in memory
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import copy
original = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

# Assignment
copy1 = original
print("Same Object ?", original is copy1, "\n")         # ✅ True  — same object, same memory address

# Shallow copy
copy2 = original.copy()
print("Same Object ?", original is copy2,)              # ❌ False — different top-level object
print("Shared Lists ?", original[0] is copy2[0], "\n") # ✅ True  — inner lists still shared

# Deep copy
copy3 = original.copy()
print("Same Object ?", original is copy3,)              # ❌ False — completely independent
print("Shared Lists ?", original[0] is copy3[0], "\n") # ✅ True  — inner lists still shared

# Tip => Use the is operator to check if the copies are truly independent

# 📌 How to Copy?
# - Avoid Assignment = (Risky + Confusing)         ⚠️ Same object — not a real copy
# - Use .copy() for simple, flat lists              🪞 Safe for 1D lists
# - Use copy.deepcopy() for nested lists            🔬 Safe for matrices / nested lists
# - Always make extra copy for experiments/tests    🧪


# ╔══════════════════════════════════════════════════════════╗
# ║  🔗  SECTION 2 — Combining Lists                        ║
# ╚══════════════════════════════════════════════════════════╝

# 3 ways to combine lists:
# ➕ + operator   → creates a NEW combined list (original untouched)
# 🔁 .extend()   → modifies the ORIGINAL list in place (no new list created)
# 🤐 zip()       → pairs items by position into a list of tuples

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

# Combine the lists
combined = letters + numbers            # ➕ Creates a brand new list — originals untouched
print("Combined : ",combined)  # ['a', 'b', 'c', 1, 2, 3]
print("Multiplied : ",letters * 2, '\n')   # 🔁 Repeats the list — useful for initializing

# Create a nested list
nested = [letters, numbers]             # 🧱 Wraps both lists inside a new list
print('Nested : ',nested, '\n')  # [['a', 'b', 'c'], [1, 2, 3]]

# extend modifies the original list
numbers.extend(letters) # 🔁 extend doesn't create a new list; it expands the original one.
print(letters)  # ['a', 'b', 'c', 1, 2, 3]
print(numbers)


# Create a list of pairs (zip)
pairs = list(zip(letters, numbers)) # 🤐 Output will always be " List Of Tupples "
print('Pairs : ',pairs, '\n')  # [('a', 1), ('b', 2), ('c', 3)]


letters2 = ['a', 'b', 'c', 'd'] 
numbers2 = [1, 2, 3]
pair2 = list(zip(letters2, numbers2))       # 🤐 Stops at shortest list — 'd' is dropped
pair3 = list(zip(letters2, numbers2, "Hi")) # 🤐 Zips 3 iterables — stops at shortest ("Hi" = 2 chars)
print(pair2)
print(pair3)


# ╔══════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 3 — Iterators & Iterables                  ║
# ╚══════════════════════════════════════════════════════════╝

# 📖 Iterable  — anything you can loop over (list, string, range...)
# 🔄 Iterator  — an object that produces values one at a time (enumerate, reversed, zip, map)
# 💡 Key difference: iterators are lazy — they don't compute until you ask (saves memory!)

# TASK
# Store the transformed results in a new list

letters = ['a', 'b', 'c']
new_list=[]

for l in letters:
    new_list.append(l.upper())  # ⬆️ Converts each letter to uppercase and stores it
    print(new_list)

# - - - - - - - - - - - - - - - - - - - - - - 
# 🔢 enumerate() — adds an automatic index counter to each item
# Useful when you need both the position AND value while looping
# - - - - - - - - - - - - - - - - - - - - - - 

letters = ['a', 'b', 'c']
print(enumerate(letters))                           # 🔄 Returns an enumerate object (lazy iterator)

print(list(enumerate(letters, start = 1)))          # 📋 Convert to list to see it | start=1 begins index at 1

for index, value in enumerate(letters):             # 🔢 Unpack both index and value in the loop
    print(index, value)

# Enumerate Use Case
# 🎯 Find the exact position of the bad data in your list

# - - - - - - - - - - - - - - - - - - - - - -
# 🔃 reversed() — loops through a list backwards without modifying the original
# - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']

print(reversed(letters))                # 🔄 Returns a reverse iterator (lazy)
print(list(reversed(letters)))          # 📋 Convert to list to see the reversed order

for l in reversed(letters):            # 🔃 Iterate in reverse — original list unchanged
    print(l)

# - - - - - - - - - - - - - - - - - - - - - -
# 🤐 zip() — pairs items from two (or more) lists by position
# Stops at the shortest list
# - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

print(zip(letters, numbers))            # 🔄 Returns a zip object (lazy iterator)
print(list(zip(letters, numbers)))      # 📋 Convert to list → list of tuples

for l, n in zip(letters, numbers):     # 🤐 Unpack each tuple pair directly in the loop
    print(l,n)

# - - - - - - - - - - - - - - - - - - - - - - 
# 🗺️ MAP
# Applies a function to EVERY item in a list — returns a new iterator
# Cleaner alternative to writing a for loop just to transform values
# - - - - - - - - - - - - - - - - - - - - - - 
letters = ['a', 'b', 'c']
print(map(str.upper, letters))              # 🔄 Returns a map object (lazy iterator)
print(list(map(str.upper, letters)))        # 📋 Convert to list → ['A', 'B', 'C']

numbers = ['1', '2', '3']
print(map(int, numbers))                    # 🔄 Lazy — nothing converted yet
print(list(map(int, numbers)))              # 🔢 Converts all string numbers → integers

# Task : Clean up the list by removing all unwanted spaces

names = [' Maria ', 'John ', ' Kumar ']
print(list(map(str.strip, names)))          # ✂️ Strips leading/trailing spaces from each name

names = [' Maria ', 'John ', ' Kumar ']
for n in map(str.strip, names):            # ✂️ Same but iterating directly — no list needed
    print(n)


# ╔══════════════════════════════════════════════════════════╗
# ║  🚦  SECTION 4 — Filter                                 ║
# ╚══════════════════════════════════════════════════════════╝

# 🚦 filter() — keeps only items that pass a condition (return True)
# Think of it as a bouncer — only truthy values get through
# filter(function, list) → applies function to each item, keeps only True results
# Passing None as the function filters out ALL falsy values (0, "", None, False)

# Task Clean up the list by removing invalid data

letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))      # 🚦 None removes all falsy values like 0, "", or False

print(list(filter(bool, letters)))      # 🚦 bool works the same! it filters out all falsy values

items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items))) # 🔤 Keeps only items made of letters — removes '123' and '42'

items = ['sql', '123', 'python', '42']
for i in filter(str.isalpha, items):   # 🔤 Same but iterating directly — no list conversion needed
    print(i)