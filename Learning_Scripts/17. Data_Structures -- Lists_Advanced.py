# ╔══════════════════════════════════════════════════════════════════════╗
# ║               📑  INDEX — Lists Fundamentals                        ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  📋  SECTION 1 — Copy                              → Line  40       ║
# ║      ⚠️  Assignment  →  same object, risky         → Line  57       ║
# ║      🪞  Shallow     →  independent, top-level     → Line  75       ║
# ║      🔬  Deep        →  fully independent          → Line 114       ║
# ║      🔍  is Operator →  same object in memory?     → Line 138       ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  🔗  SECTION 2 — Combining Lists                   → Line 181       ║
# ║      ➕  +           →  creates a new combined list → Line 198      ║
# ║      🧱  nested      →  wrap lists inside a list   → Line 203       ║
# ║      🔁  .extend()   →  expands original in place  → Line 207       ║
# ║      🤐  zip()       →  pairs items by position    → Line 214       ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  🔄  SECTION 3 — Iterators & Iterables             → Line 230       ║
# ║      🔢  enumerate() →  index counter per item     → Line 255       ║
# ║      🔃  reversed()  →  loops backwards, safe      → Line 276       ║
# ║      🤐  zip()       →  pairs items while looping  → Line 293       ║
# ║      🗺️  map()       →  transforms every item      → Line 311       ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  🚦  SECTION 4 — Filter                            → Line 338       ║
# ║      🚦  filter()    →  keeps only truthy items    → Line 354       ║
# ║      🔤  str.isalpha →  keeps only alpha items     → Line 360       ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  ⚡  SECTION 5 — Lambda                            → Line 372       ║
# ║      ⚡  lambda       →  anonymous one-line fn      → Line 391      ║
# ║      🗺️  map+lambda  →  transform every item       → Line 408       ║
# ║      🚦  filter+lambda→  keep items that pass      → Line 436       ║
# ║      🔃  sorted+lambda→  sort by custom key        → Line 455       ║
# ╠══════════════════════════════════════════════════════════════════════╣
# ║  🧩  SECTION 6 — List Comprehension                → Line 481       ║
# ║      🔁  basic       →  [ x for x in list ]        → Line 512       ║
# ║      🚦  with filter →  [ x for x in list if cond ]→ Line 514       ║
# ║      🔄  transform   →  [ f(x) for x in list ]     → Line 513       ║
# ╚══════════════════════════════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════╗
# ║  📋  SECTION 1 — Copy                                   ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📖 WHY COPYING MATTERS
# When you work with lists, you often need to keep the original safe
# while experimenting or transforming a copy. Python gives you 3 ways:
#
#   ⚠️  Assignment ( = )       →  NOT a real copy. Both names share the same list.
#   🪞  Shallow ( .copy() )    →  New list, but inner objects are still shared.
#   🔬  Deep ( deepcopy() )    →  Everything duplicated. Fully safe.
#
# Rule of thumb:
#   Flat list?     →  .copy() is enough
#   Nested list?   →  always use deepcopy()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ⚠️  ASSIGNMENT COPY  ( = )
#
# This is NOT a copy — it is an alias.
# Both variables point to the EXACT same list object in memory.
# There is only one list. Changing it via either name changes it for both.
# Avoid this pattern unless you intentionally want two names for one list.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']
letters_copy = letters          # ⚠️ Not a real copy — both point to the same list in memory
letters.pop()                   # 🗑️ Removes last item from 'letters' — affects letters_copy too!
letters_copy.append('z')        # ➕ Appends to letters_copy — affects letters too!

print(f"Original : {letters} \nCopy : {letters_copy}")
# 💡 Both print the same thing — they ARE the same list


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 🪞  SHALLOW COPY  ( .copy() )
#
# Creates a brand new list object at the TOP level.
# For flat (non-nested) lists, this is completely safe — changes don't bleed through.
# ⚠️  Gotcha: for nested lists, the inner lists are still SHARED between original and copy.
#     A shallow copy only duplicates the outer container, not what's inside it.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']
letters_copy = letters.copy()   # 🪞 Real independent copy — changes won't cross over
letters.pop()                   # 🗑️ Only affects 'letters'
letters_copy.append('z')        # ➕ Only affects 'letters_copy'

print(f"Original : {letters} \nCopy : {letters_copy}")
# ✅ Different results — they are independent at the top level

# - - - - - - - - - - - - - - - - - - - - - -
# ⚠️  SHALLOW COPY TRAP — Nested Lists
#
# matrix.copy() creates a new outer list,
# but each inner row (e.g. ['a','b','c']) is still the SAME object in memory.
# Appending to a row via the copy also modifies the original's row.
# - - - - - - - - - - - - - - - - - - - - - -

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix_copy = matrix.copy()
matrix.pop()                        # 🗑️ Removes Row 2 — only affects original (top-level change)
matrix_copy[0].append('z')          # ⚠️ Only Top Level Is Copied, And Deep Level Is Shared, Hence Any Update On Copy Would Reflect On Original On This Scenario 

print(f"Original : {matrix} \nCopy : {matrix_copy}")
# ⚠️  Notice Row 0 of the original also has 'z' — the inner list is shared!


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 🔬  DEEP COPY  ( copy.deepcopy() )
#
# Recursively duplicates every object — outer list AND all inner lists.
# The copy is 100% independent. No shared references at any level.
# This is the safe choice whenever your list contains other lists (matrices, tables, etc.)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import copy                         # 📦 Standard library — no install needed
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
# ✅ Original is untouched — deepcopy broke the shared reference


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 🔍  IS OPERATOR
#
# == checks if two variables have the SAME VALUE
# is checks if two variables point to the SAME OBJECT in memory (same address)
#
# A variable can have the same value as another but still be a different object.
# Use `is` to verify whether a copy is truly independent or still linked.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import copy
original = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

# ── Assignment ─────────────────────────────────────────────
copy1 = original
print("Same Object ?", original is copy1, "\n")         # ✅ True  — same object, same memory address

# ── Shallow copy ───────────────────────────────────────────
copy2 = original.copy()
print("Same Object ?", original is copy2,)              # ❌ False — different top-level object
print("Shared Lists ?", original[0] is copy2[0], "\n") # ✅ True  — inner lists still shared

# ── Deep copy ──────────────────────────────────────────────
copy3 = original.copy()
print("Same Object ?", original is copy3,)              # ❌ False — completely independent
print("Shared Lists ?", original[0] is copy3[0], "\n") # ✅ True  — inner lists still shared

# Tip => Use the is operator to check if the copies are truly independent

# ┌─────────────────────────────────────────────────────────┐
# │  📌  Quick Copy Decision Guide                          │
# │                                                         │
# │  Avoid  =          ⚠️  Same object — not a real copy   │
# │  Use .copy()       🪞  Safe for flat / 1D lists         │
# │  Use deepcopy()    🔬  Safe for nested / matrix lists   │
# │  Extra copy        🧪  Always good for experiments      │
# └─────────────────────────────────────────────────────────┘


# ╔══════════════════════════════════════════════════════════╗
# ║  🔗  SECTION 2 — Combining Lists                        ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📖 3 WAYS TO COMBINE
#
#   ➕  +           →  Creates a NEW list. Originals stay untouched.
#   🔁  .extend()   →  Modifies the ORIGINAL list in place. No new object.
#   🤐  zip()       →  Pairs items by position. Stops at shortest list.
#
# Choose + when you want to keep originals safe.
# Choose .extend() when you want to grow a list efficiently (no extra object).
# Choose zip() when you want to work with two lists side-by-side.


letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

# ── + Operator ─────────────────────────────────────────────
combined = letters + numbers            # ➕ Creates a brand new list — originals untouched
print("Combined : ",combined)  # ['a', 'b', 'c', 1, 2, 3]
print("Multiplied : ",letters * 2, '\n')   # 🔁 Repeats the list — useful for initializing

# ── Nested List ────────────────────────────────────────────
nested = [letters, numbers]             # 🧱 Wraps both lists inside a new list
print('Nested : ',nested, '\n')  # [['a', 'b', 'c'], [1, 2, 3]]

# ── .extend() ──────────────────────────────────────────────
# 💡 Unlike +, extend doesn't create a new list.
#    It pushes items from one list directly into another — more memory-efficient.
numbers.extend(letters) # 🔁 extend doesn't create a new list; it expands the original one.
print(letters)  # ['a', 'b', 'c', 1, 2, 3]
print(numbers)

# ── zip() ──────────────────────────────────────────────────
# 💡 zip always produces a list of TUPLES — one tuple per position.
#    If lists are different lengths, it stops at the shortest one (items are dropped).
pairs = list(zip(letters, numbers)) # 🤐 Output will always be " List Of Tupples "
print('Pairs : ',pairs, '\n')  # [('a', 1), ('b', 2), ('c', 3)]

# ── zip with uneven lengths ────────────────────────────────
letters2 = ['a', 'b', 'c', 'd'] 
numbers2 = [1, 2, 3]
pair2 = list(zip(letters2, numbers2))       # 🤐 Stops at shortest list — 'd' is dropped
pair3 = list(zip(letters2, numbers2, "Hi")) # 🤐 Zips 3 iterables — stops at shortest ("Hi" = 2 chars)
print(pair2)
print(pair3)


# ╔══════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 3 — Iterators & Iterables                  ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📖 KEY CONCEPTS
#
#   📖  Iterable  →  Anything you can loop over: list, string, range, dict...
#   🔄  Iterator  →  An object that yields values ONE AT A TIME on demand.
#                    (enumerate, reversed, zip, map are all iterators)
#
#   💡  Iterators are LAZY — they compute nothing until you ask.
#       This saves memory, especially on large datasets.
#       Wrap with list() to see all values at once, or loop directly.


# ── Manual loop approach (baseline) ───────────────────────
# 🎯 Classic for-loop: build a new list by appending transformed items one by one.
letters = ['a', 'b', 'c']
new_list=[]

for l in letters:
    new_list.append(l.upper())  # ⬆️ Converts each letter to uppercase and stores it
    print(new_list)


# - - - - - - - - - - - - - - - - - - - - - -
# 🔢  enumerate()
#
# Wraps any iterable and attaches an auto-incrementing index to each item.
# Returns pairs of (index, value) — you unpack them in the loop header.
# Use start= to begin counting from any number (default is 0).
# Perfect for: tracking position, finding bad data, numbered output.
# - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']
print(enumerate(letters))                           # 🔄 Returns an enumerate object (lazy iterator)

print(list(enumerate(letters, start = 1)))          # 📋 Convert to list to see it | start=1 begins index at 1

for index, value in enumerate(letters):             # 🔢 Unpack both index and value in the loop
    print(index, value)

# Enumerate Use Case
# 🎯 Find the exact position of the bad data in your list


# - - - - - - - - - - - - - - - - - - - - - -
# 🔃  reversed()
#
# Returns a reverse iterator — loops through the list from last to first.
# Does NOT modify the original list (unlike list.reverse() which does).
# Lazy: doesn't create a new reversed list in memory unless you wrap with list().
# - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']

print(reversed(letters))                # 🔄 Returns a reverse iterator (lazy)
print(list(reversed(letters)))          # 📋 Convert to list to see the reversed order

for l in reversed(letters):            # 🔃 Iterate in reverse — original list unchanged
    print(l)


# - - - - - - - - - - - - - - - - - - - - - -
# 🤐  zip()  (as iterator)
#
# Pairs up items from multiple iterables by position.
# Returns an iterator of tuples — lazy until consumed.
# Unpack the tuple directly in the loop header for clean code.
# - - - - - - - - - - - - - - - - - - - - - -

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

print(zip(letters, numbers))            # 🔄 Returns a zip object (lazy iterator)
print(list(zip(letters, numbers)))      # 📋 Convert to list → list of tuples

for l, n in zip(letters, numbers):     # 🤐 Unpack each tuple pair directly in the loop
    print(l,n)


# - - - - - - - - - - - - - - - - - - - - - -
# 🗺️  map()
#
# Applies a function to EVERY item in an iterable — returns a lazy iterator.
# A cleaner, more readable alternative to a for-loop when you just want to transform.
# The function can be a built-in (str.upper, int, str.strip) or a custom one.
# Wrap with list() to materialise all results at once.
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
#
# 📖 WHAT IS filter()?
#
# Think of filter() as a bouncer at the door.
# It runs each item through a function — only items that return True get in.
#
#   filter(function, iterable)
#   └─ function  →  called on each item; must return True to keep it
#   └─ None      →  special shortcut: removes all falsy values (0, "", None, False, [])
#
# Like map(), it returns a lazy iterator — wrap with list() or loop directly.
# Passing None is the fastest way to strip out all falsy/empty values.


# ── Clean up: remove falsy values ──────────────────────────
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))      # 🚦 None removes all falsy values like 0, "", or False

print(list(filter(bool, letters)))      # 🚦 bool works the same! it filters out all falsy values

# ── Keep only alphabetic strings ───────────────────────────
# 💡 str.isalpha returns True only if every character in the string is a letter.
#    Numbers like '123' and '42' return False and are dropped.
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items))) # 🔤 Keeps only items made of letters — removes '123' and '42'

items = ['sql', '123', 'python', '42']
for i in filter(str.isalpha, items):   # 🔤 Same but iterating directly — no list conversion needed
    print(i)


# ╔══════════════════════════════════════════════════════════╗
# ║  ⚡  SECTION 5 — Lambda                                 ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📖 LAMBDA vs NORMAL FUNCTION
#
#   def double(x):          ←  Named function: reusable, multi-line, has docstring
#       return x * 2
#
#   lambda x: x * 2         ←  Anonymous function: one-liner, auto-returns, throwaway
#
# Key rules for lambda:
#   • No def, no return keyword — the expression IS the return value
#   • One expression only — no multiple statements, no if/else blocks*
#   • Can be assigned to a variable, but that defeats the "anonymous" purpose
#   • Best used INLINE inside map(), filter(), sorted()
#
# *Ternary expressions (a if cond else b) ARE allowed — they count as one expression.


# ── Basic lambda ───────────────────────────────────────────

multiply = lambda x: x * 2             # ⚡ lambda x  → takes one argument, returns x * 2
print(multiply(2))

add = lambda x, y: x + y               # ⚡ lambda x, y → takes two arguments, returns their sum
print(add(1, 2))

# NOTE
# A lambda can contain any expression, including conditions

check = lambda i: i in "python"        # ⚡ Returns True if character exists in the string "python"
print(check('n'))                      # ✅ True  — 'n' is in "python"
print(check('z'))                      # ❌ False — 'z' is not in "python"


# - - - - - - - - - - - - - - - - - - - - - -
# 🗺️  Lambda + map()
#
# map() needs a function — lambda lets you write it inline without naming it.
# This combo is great for one-off transformations you won't reuse elsewhere.
# Chain method calls inside the lambda expression for multi-step cleaning.
# - - - - - - - - - - - - - - - - - - - - - -

prices = ['$12.50', '$9.99', '$100.00']

# Using map with lambda to clean all prices
cleaned_prices = list(map(lambda p: float(p.replace('$', '').strip()), prices))  # 🗺️ Strips '$' and converts to float
print(cleaned_prices)  # [12.5, 9.99, 100.0]

# Alternative using list comprehension
cleaned_prices = [float(p.replace('$', '').strip()) for p in prices]   # 📋 Same result, different style
print(cleaned_prices)  # [12.5, 9.99, 100.0]

prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

# 💡 Reading the expression step by step:
#map(lambda p: float(p.replace('$', '')), prices)
#             ^                            ^
#             |                            |
#             expression ends here         map ends here 


# - - - - - - - - - - - - - - - - - - - - - -
# 🚦  Lambda + filter()
#
# filter() needs a function that returns True/False — lambda fits perfectly.
# Write your condition inline: no need to define a separate def function.
# Access nested data (like row[1]) directly inside the lambda.
# - - - - - - - - - - - - - - - - - - - - - -

prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >=100, prices)))  # 🚦 Keeps only prices >= 100 → [120, 300]


students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]

print(list(filter(lambda row: row[1] > 70, students)))  # 🚦 Keeps only students with score > 70


# - - - - - - - - - - - - - - - - - - - - - -
# 🔃  Lambda + sorted()
#
# sorted() returns a NEW sorted list — original is untouched.
# key= tells it what to sort BY — lambda extracts the sort field from each item.
# Access any field: row[0] for name, row[1] for score, len(x) for length, etc.
# - - - - - - - - - - - - - - - - - - - - - -

students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]

# Task : Students Only With M

students = [['Maria', 85],
            ['Kumar', 90],
            ['Max', 60]]

# ── startswith() — checking the condition before filtering ─
print(students[0][0].startswith('M'))   # ✅ True  — 'Maria' starts with 'M'
print(students[1][0].startswith('M'))   # ❌ False — 'Kumar' does not
print(students[2][0].startswith('M'))   # ✅ True  — 'Max' starts with 'M'

print(list(filter(lambda row: row[0].startswith('M'), students)))  # 🚦 Keeps only students whose name starts with 'M'


# ╔══════════════════════════════════════════════════════════╗
# ║  🧩  SECTION 6 — List Comprehension                     ║
# ╚══════════════════════════════════════════════════════════╝
#
# 📖 WHAT IS LIST COMPREHENSION?
#
# A concise, readable way to build a new list — combining a loop,
# an optional filter, and a transformation into a single expression.
#
#   [ expression   for item in iterable   if condition ]
#         │               │                     │
#    what to keep    loop variable          optional gate
#
# Equivalent to:
#   result = []
#   for item in iterable:
#       if condition:
#           result.append(expression)
#
# 💡 Prefer comprehensions over map+lambda when the logic is readable in one line.
#    Use map/filter when you need lazy evaluation on large datasets.
#
# Structure breakdown for the example below:
#   d.lower().replace('www.', '')  →  🔄 Transform: clean the domain string
#   for d in domains               →  🔁 Loop: iterate over every domain
#   if '.' in d                    →  🚦 Filter: skip entries without a dot (e.g. 'localhost')

domains = ['www.google.com',
          'openai.com',
          'localhost',
          'AKASHSAHA-PROFILE.NETLYFY.APP']

cleaned = [
    d.lower().replace('www.', '')   # Data Transformation
    for d in domains                # For Loop
    if '.' in d                     # Data Filtering
]

print(cleaned)
# ✅ Output: ['google.com', 'openai.com', 'akashsaha-profile.netlyfy.app']
# 💡 'localhost' is dropped — it has no '.' in it