# ═══════════════════════════════════════════════════════════
#   PYTHON DATA STRUCTURES — Quick Reference
# ═══════════════════════════════════════════════════════════

# ── LIST  →  Square Brackets [ ] ────────────────────────────
# my_list = [10, 20, 15]
#
# ✅ Common — most used data structure
# ✅ Ordered, Indexed, Allows duplicates
# ✅ Mutable / Changable — you CAN add, remove, change items
# Syntax: [m, m, m]

# ── TUPLE  →  Parentheses ( ) ───────────────────────────────
# my_tuple = (10, 20, 15)
#
# 🔒 No Changes! — Immutable
# ✅ Ordered, Indexed, Allows duplicates
# ❌ Cannot add, remove, or change items after creation
# Syntax: (m, m, m)

# ── SET  →  Curly Brackets { } ──────────────────────────────
# my_set = {10, 20, 15}
#
# 👆 Unique! — No duplicate values allowed
# ❌ Unordered — no guaranteed index
# ✅ Mutable — can add/remove, but no duplicates stored
# Syntax: {m, m, m}

# ── DICT  →  Curly Brackets { key : value } ─────────────────
# my_dict = {'a': 10, 'b': 20, 'c': 15}
#
# 🔑 Key : Value pairs
# ✅ Keys must be unique
# ✅ Ordered (Python 3.7+), Mutable
# Syntax: {m: m, m: m}

# ═══════════════════════════════════════════════════════════
#   CHEAT SHEET
#   [ ]  →  List   — ordered, changeable, duplicates OK
#   ( )  →  Tuple  — ordered, LOCKED,     duplicates OK
#   { }  →  Set    — unordered, changeable, NO duplicates
#   {:}  →  Dict   — key:value pairs,      keys unique
# ═══════════════════════════════════════════════════════════


# ╔══════════════════════════════════════════════════════════╗
# ║  🚀  SECTION 1 — CREATING LISTS                         ║
# ╚══════════════════════════════════════════════════════════╝

# ------------------------------------------------------------------
# ── LIST  →  Square Brackets [ ] ────────────────────────────
# ------------------------------------------------------------------
# Create an list

empty = []                         # 🗒️ Empty list — ready to be filled
print(empty)
print(type(empty))
# ---------------------------
letters = ['a', 'b', 'c']         # 🔤 List of characters
print(letters)
print(type(letters))
# ---------------------------
numbers = [1,2,3,4]               # 🔢 List of integers
print(numbers)
print(type(numbers))
# ---------------------------
mixed = [1, 'a', True, None]      # 🎨 Lists can hold ANY type together
print(mixed)
print(type(mixed))

# ------------------------------------------------------------------
# Creating list out of string value
# ------------------------------------------------------------------

letters = list('Python')          # 🔄 Converts each character into a list item → ['P','y','t','h','o','n']
print(letters)

numbers = list(range(5))          # 🔄 Converts range into a list → [0, 1, 2, 3, 4]
print(numbers)

# ------------------------------------------------------------------
# ── NESTED LIST / Matrix
# ------------------------------------------------------------------

matrix = [['a', 'b', 'c'],          # 🧱 A list inside a list — like rows in a table
          ['d','e', 'f']]
print(matrix)
print(type(matrix))

mixed_matrix = [['a', 'b', 'c'],   # 🎭 Each row can hold different types too
                [1, 2, 3],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))


# ╔══════════════════════════════════════════════════════════╗
# ║  🔍  SECTION 2 — INDEXING & SLICING                     ║
# ╚══════════════════════════════════════════════════════════╝

# ------------------------------------------------------------------
# Access & Read
# ------------------------------------------------------------------
# 📌 Index starts at 0 from the left, -1 from the right

lst = ['A', 'B', 'C', 'D']

print(lst)
print(len(lst))        # 📏 Total number of items

print(lst[0])          # 👈 First item
print(lst[-1])         # 👉 Last item — negative index counts from the end
print(lst[3])          # 👉 4th item

# ------------------------------------------------------------------
# Access & Read Inside Matrix
# ------------------------------------------------------------------
# 🗺️ Think of it as [row][column]

matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i'] # Row 2
]
print(matrix)
print(matrix[2])           # 📍 Entire Row 2    #/ print(matrix[-1])
print(matrix[-1][2])       # 📍 Last row, last item  #/ print(matrix[-1][-1])
print(matrix[0][0])        # 📍 First row, first item
print(matrix[1][1])        # 📍 Middle item     #/ print(matrix[-2][-2])

# ------------------------------------------------------------------
# Slicing / Multiple Items Retrieve
# ------------------------------------------------------------------
# ✂️ Syntax: list[start:stop] — 'stop' index is NOT included

lst = ['a', 'b', 'c', 'd']
print(lst[:2])    # ✂️ From start up to index 2 (not included)
print(lst[2:])    # ✂️ From index 2 to end
print(lst[:])     # 📋 Full copy of the list


# ╔══════════════════════════════════════════════════════════╗
# ║  📦  SECTION 3 — UNPACKING LISTS                        ║
# ╚══════════════════════════════════════════════════════════╝

# =========================================================
# UNPACKING LISTS 📦 -> ✨
# =========================================================
person = ['Akash', 29, 'Data Analyst', 'Spain']
# Instead of doing this:
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

# Do this (Unpacking):
name, age, role, country = person
print(role)  # Output: Data Engineer

# =========================================================

# ------------------------------------------------------------------
# Rest Collector
# Asterisk *
# ------------------------------------------------------------------
# ⭐ The * (star) operator "vacuums up" whatever doesn't fit into named variables

person = ['Akash', 29, 'Data Analyst', 'India']

name, *details, country = person   # ⭐ 'details' collects everything in between
print(name)
print(details)
print(country)
# ---------------------------------
person = [1, 'Akash', 29, 'Data Analyst', 'India']
name, *details, country = person
print(name)
print(details)
print(country)
# ---------------------------------
person = ['Akash', 29, 'Data Analyst', 'India']
name, *details = person            # ⭐ Star at the end — collects all remaining items
print(name)
print(details)

person = ['Akash', 29, 'Data Analyst', 'India']
*details, country  = person        # ⭐ Star at the start — collects all leading items
print(details)
print(country)


# =========================================================
# PYTHON UNPACKING RULES 📜
# =========================================================

# RULE 1: Exact Match ⚖️
# The number of variables must match the values exactly.
# Not less, not more.
numbers = [1, 2, 3, 4]

# This would raise: ValueError: too many values to unpack
# first, second, third, fourth, last = numbers 


# RULE 2: The Asterisk (*) "Catch-All" 🪣
# The asterisk collects 'leftovers' into a new list. 
# It's fine if there are no leftovers (it will just be empty).
numbers = [1]

first, *rest = numbers

print(first) # Output: 1
print(rest)  # Output: [] (Empty list because nothing was left)


# PRO TIP: You can use * anywhere!
# first, *middle, last = [1, 2, 3, 4, 5]
# middle would be [2, 3, 4]
# =========================================================

# =========================================================
# THE UNDERSCORE OPERATOR (_) 🐍
# =========================================================
# 🗑️ Use _ to intentionally IGNORE values you don't need

person = ['Akash', 29, 'Data Analyst', 'India']

name, _ , _ , country = person
print(name)
print(country)

# ---------------------------------
person = ['Akash', 29, 'Data Analyst', 'India']

name, *_, country = person         # 🗑️ *_ throws away everything between name and country
print(name)
print(country)


# ╔══════════════════════════════════════════════════════════╗
# ║  🔬  SECTION 4 — EXPLORE & ANALYZE                      ║
# ╚══════════════════════════════════════════════════════════╝

# =========================================================
# Explore & Analyze Lists 🐍
# =========================================================

# (13 Hours) = From Zero to Hero

# ## Analyze
# 2 5 800 → max() → 800
# Find extreme High

# 800 2 300 → min() → 2
# Find extreme low

# 2 3 5 → Sum() → 10
# Find the Total

# 1 2 3 → len() → 3
# Find the Length

# ---

# ## Completeness & Existence Check
# A' b 30 → all() → True
# Did Everything Pass?

# A x x → any() → True
# Did Something Pass?

# ---

# ## Search Count
# A B A' B' A' B' C' → .Count(A') → 2
# How often?

# A B A' B' → index(A') → 0
# Where it appears?

# ---

# ## Membership Identity
# 'A' in 'A' 'B' → True
# Check if it exists!

# 'A' is 'A' 'B' → False
# Check if same object!

# ---

# ## Comparison
# 'A' 'B' == 'A' 'B' → True

# 'A' 'B' > 'A' 'B' → False

# =========================================================
# Explore & Analyze Lists 🐍
# =========================================================

numbers = [1, 5, 5, 4, 3]

# 📊 Numeric Aggregations
print("Max : ", max(numbers))      # 🔺 Highest value
print("Min : ", min(numbers))      # 🔻 Lowest value
print("Sum : ", sum(numbers))      # ➕ Total of all values
print("Length : ", len(numbers))   # 📏 How many items

# ✅ all() — True ONLY if every value is truthy (non-zero, non-empty)
print("All : ", all([numbers]))         # ✅ True
print("All : ", all([1, 0, 2]))         # ❌ False — 0 is falsy
print("All : ", all(['a', 'b', 'c']))   # ✅ True
print("All : ", all(['a', '', 'c']))    # ❌ False — '' (empty string) is falsy

# 🔍 any() — True if AT LEAST one value is truthy
print("All : ", any([numbers]))         # ✅ True
print("All : ", any([1, 0, 2]))         # ✅ True — 1 and 2 are truthy
print("All : ", any(['a', 'b', 'c']))   # ✅ True
print("All : ", any(['a', '', 'c']))    # ✅ True — 'a' and 'c' are truthy

# 🔎 Search & Count
print("Count : ", numbers.count(5))    # 🔢 How many times does 5 appear?
print("Count : ", numbers.index(5))    # 📍 Returns only the first appearance

# 🪪 Membership
print(4 in numbers)      # ✅ True  — 4 is in the list
print(8 in numbers)      # ❌ False — 8 is not in the list

print(4 not in numbers)  # ❌ False — because 4 IS in the list
print(8 not in numbers)  # ✅ True  — because 8 is NOT in the list

# ⚖️ Equality (same values) vs Identity (same object in memory)
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)    # ✅ True  — same values
print(list1 is list2)    # ❌ False — different objects in memory

list3 = [1,2,3,4]
list4 = [1,2,3]
print(list3 == list4)    # ❌ False — different lengths

# 📐 Comparison — compares element by element, left to right
list5 = [1,2,3]
list6 = [5,2,3]
print(list5 < list6)     # ✅ True  — 1 < 5


# ╔══════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 5 — CHANGING LISTS (Add / Remove / Update) ║
# ╚══════════════════════════════════════════════════════════╝

# =========================================================
# Changing Lists In 🐍
# =========================================================

# ➕ ADDING TO LISTS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# .append(value)    → Adds to the END of the list
# .insert(i, value) → Adds at a SPECIFIC index (pushes others right)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
letters = ['a', 'b', 'c', 'd']

letters.append('x')               # ➕ Adds 'x' to the end
letters.append('y')               # ➕ Adds 'y' to the end

letters.insert(1,'f')             # 📌 Inserts 'f' at index 1 (shifts others right)
letters.insert(3,'g')             # 📌 Inserts 'g' at index 3

print(letters)

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix.append(['x', 'y', 'z'])        # ➕ Adds a new row at the end
matrix.insert(0, ['k', 'l', 'm'])     # 📌 Inserts new row at the top (index 0)
matrix.append(['End_List',])          # ➕ Adds a single-item row at the end

# Add new items inside Row 1
matrix[1].append('x')                 # ➕ Appends 'x' to Row 1
matrix[0].insert(3,'Z')               # 📌 Inserts 'Z' at index 3 of Row 0
matrix[1].insert(2,'E')               # 📌 Inserts 'E' at index 2 of Row 1

print(matrix)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ➖ REMOVING FROM LISTS
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# .clear()          → 🗑️ Remove ALL items (empties the list)
# .remove(value)    → 🎯 Remove by VALUE — only removes the FIRST match
# .pop(index)       → 📤 Remove & RETURN by position (default = last item)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
letters = ['a', 'b', 'c', 'd', 'a']

letters.remove('a')   # 🎯 Removes only first 'a'
letters.remove('a')   # 🎯 Removes 2nd 'a' in List
print(letters)

# ************************************************
letters2 = ['a', 'b', 'c', 'd', 'a']
letters2.clear()    # 🗑️ Clears The Entire List
print(letters2)

# ************************************************
letters3 = ['a', 'b', 'c', 'd', 'a']

removed = letters3.pop(2)      # 📤 Remove & return by position
removed2 = letters3.pop()      # 📤 Default — removes & returns the last item
print(letters3)
print("Removed Item : ", removed)
print("Removed Item : ", removed2)

# ************************************************
matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i'] # Row 2
]

# matrix.remove(['a', 'b', 'c'])
matrix[1].pop(1)      # 📤 Removes item at index 1 from Row 1  # Or we can use  matrix[1].pop('e')
matrix[-1].pop(0)     # 📤 Removes first item from last row
matrix[-3].pop(2)     # 📤 Removes item at index 2 from first row
# matrix.pop()        # 📤 Removes Last List As Default
print(matrix)


# =========================================================
# ✏️ Updating Lists
# =========================================================
# ⚠️ Always use an index to update a specific item.
#    Assigning without an index replaces the list variable entirely!
# To update one value , need to specify an index otherwise the whole list needs will get updated

letters = ['a', 'b', 'c', 'd', 'e']

letters[0] = 'x'    # ✏️ Updates index 0 from 'a' → 'x'
letters[1] = 'y'    # ✏️ Updates index 1 from 'b' → 'y'

print(type(letters))
print(letters)

# ************************************************
letters2 = ['a', 'b', 'c', 'd', 'e']
letters2 = 'z'          # ⚠️ This REPLACES the list entirely — letters2 is now a string!
print(type(letters2))
print(letters2)

# ************************************************
matrix = [
    ['a', 'b', 'c'], # Row 0
    ['d', 'e', 'f'], # Row 1
    ['g', 'h', 'i'] # Row 2
]

matrix[2] = ['x', 'y', 'z']   # ✏️ Replaces the entire Row 2
matrix[0][0] = '-'             # ✏️ Updates individual cell → Row 0, Col 0
matrix[0][1] = '+'             # ✏️ Updates individual cell → Row 0, Col 1
matrix[0][2] = '%'             # ✏️ Updates individual cell → Row 0, Col 2
print(matrix)