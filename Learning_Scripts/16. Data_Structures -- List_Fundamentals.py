# ═══════════════════════════════════════════════════════════════════════════════
#   PYTHON DATA STRUCTURES — Quick Reference
#   File   : python_lists_notes.py
#   Topic  : Lists — Full Deep Dive
#   Author : Akash Saha
# ═══════════════════════════════════════════════════════════════════════════════

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                          📋  PAGE INDEX                                    │
# ├─────────────────────────────────────────────────────────────────────────────┤
# │                                                                             │
# │  OVERVIEW — Data Structure Cheat Sheet              → Line  59              │
# │  ├── List   [ ]   → Ordered, Mutable, Duplicates OK                         │
# │  ├── Tuple  ( )   → Ordered, Immutable, Duplicates OK                       │
# │  ├── Set    { }   → Unordered, Mutable, NO Duplicates                       │
# │  └── Dict   {:}   → Key:Value pairs, Keys Unique                            │
# │                                                                             │
# │  SECTION 1 — CREATING LISTS                         → Line 109              │
# │  ├── 1.1  Empty List                                → Line 113              │
# │  ├── 1.2  List of Characters                        → Line 123              │
# │  ├── 1.3  List of Integers                          → Line 131              │
# │  ├── 1.4  Mixed Type List                           → Line 139              │
# │  ├── 1.5  list() from String & range()              → Line 149              │
# │  └── 1.6  Nested List / Matrix                      → Line 160              │
# │                                                                             │
# │  SECTION 2 — INDEXING & SLICING                     → Line 178              │
# │  ├── 2.1  Positive & Negative Indexing              → Line 182              │
# │  ├── 2.2  Indexing Inside a Matrix                  → Line 201              │
# │  └── 2.3  Slicing — start:stop syntax               → Line 218              │
# │                                                                             │
# │  SECTION 3 — UNPACKING LISTS                        → Line 232              │
# │  ├── 3.1  Basic Unpacking                           → Line 236              │
# │  ├── 3.2  Rest Collector  →  Asterisk *             → Line 254              │
# │  ├── 3.3  Unpacking Rules                           → Line 290              │
# │  └── 3.4  Underscore Operator _ (Ignore Values)     → Line 315              │
# │                                                                             │
# │  SECTION 4 — EXPLORE & ANALYZE                      → Line 337              │
# │  ├── 4.1  Numeric Aggregations  →  max / min / sum  → Line 360              │
# │  ├── 4.2  Completeness Check   →  all() / any()     → Line 369              │
# │  ├── 4.3  Search & Count       →  .count() .index() → Line 389              │
# │  ├── 4.4  Membership           →  in / not in       → Line 399              │
# │  ├── 4.5  Equality vs Identity →  == vs is          → Line 411              │
# │  └── 4.6  Comparison           →  element-by-element→ Line 427              │
# │                                                                             │
# │  SECTION 5 — CHANGING LISTS (Add / Remove / Update) → Line 438              │
# │  ├── 5.1  Adding    →  .append() / .insert()        → Line 442              │
# │  ├── 5.2  Removing  →  .remove() / .pop() / .clear()→ Line 476              │
# │  └── 5.3  Updating  →  index assignment             → Line 518              │
# │                                                                             │
# │  SECTION 6 — SORTING                                → Line 553              │
# │  ├── 6.1  .sort()     →  Sorts in place             → Line 557              │
# │  ├── 6.2  sorted()    →  Returns new sorted list    → Line 592              │
# │  └── 6.3  .reverse()  →  Flips list in place        → Line 603              │
# │                                                                             │
# └─────────────────────────────────────────────────────────────────────────────┘


# ═══════════════════════════════════════════════════════════
#   DATA STRUCTURE OVERVIEW — CHEAT SHEET
# ═══════════════════════════════════════════════════════════

# ── LIST  →  Square Brackets [ ] ────────────────────────────
# my_list = [10, 20, 15]
#
# ✅ Common — most used data structure
# ✅ Ordered — items stay in the order you put them
# ✅ Indexed — access items using [0], [1], [-1], etc.
# ✅ Allows duplicates — same value can appear multiple times
# ✅ Mutable / Changeable — you CAN add, remove, change items
# Syntax: [item, item, item]

# ── TUPLE  →  Parentheses ( ) ───────────────────────────────
# my_tuple = (10, 20, 15)
#
# 🔒 No Changes! — Immutable (frozen after creation)
# ✅ Ordered, Indexed, Allows duplicates
# ❌ Cannot add, remove, or change items after creation
# 💡 Use when data should NOT change (e.g. coordinates, config)
# Syntax: (item, item, item)

# ── SET  →  Curly Brackets { } ──────────────────────────────
# my_set = {10, 20, 15}
#
# 👆 Unique! — No duplicate values stored (auto-removed)
# ❌ Unordered — no guaranteed position or index
# ✅ Mutable — can add/remove, but duplicates are never stored
# 💡 Use for unique checks, filtering, membership testing
# Syntax: {item, item, item}

# ── DICT  →  Curly Brackets { key : value } ─────────────────
# my_dict = {'a': 10, 'b': 20, 'c': 15}
#
# 🔑 Key : Value pairs — like a real dictionary (word → meaning)
# ✅ Keys must be unique — values can repeat
# ✅ Ordered (Python 3.7+), Mutable
# 💡 Use when you want to label/name your data
# Syntax: {key: value, key: value}

# ═══════════════════════════════════════════════════════════
#   QUICK CHEAT SHEET
#   [ ]  →  List   — ordered, changeable, duplicates OK
#   ( )  →  Tuple  — ordered, LOCKED,     duplicates OK
#   { }  →  Set    — unordered, changeable, NO duplicates
#   {:}  →  Dict   — key:value pairs,      keys unique
# ═══════════════════════════════════════════════════════════


# ╔══════════════════════════════════════════════════════════╗
# ║  🚀  SECTION 1 — CREATING LISTS                         ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# 1.1  Empty List
# ──────────────────────────────────────────────────────────
# Start with an empty list when you plan to fill it later
# (e.g. collecting results in a loop)

empty = []                         # 🗒️ Empty list — ready to be filled
print(empty)                       # Output: []
print(type(empty))                 # Output: <class 'list'>

# ──────────────────────────────────────────────────────────
# 1.2  List of Characters
# ──────────────────────────────────────────────────────────

letters = ['a', 'b', 'c']         # 🔤 List of single characters (strings)
print(letters)                     # Output: ['a', 'b', 'c']
print(type(letters))               # Output: <class 'list'>

# ──────────────────────────────────────────────────────────
# 1.3  List of Integers
# ──────────────────────────────────────────────────────────

numbers = [1, 2, 3, 4]            # 🔢 List of whole numbers
print(numbers)                     # Output: [1, 2, 3, 4]
print(type(numbers))               # Output: <class 'list'>

# ──────────────────────────────────────────────────────────
# 1.4  Mixed Type List
# ──────────────────────────────────────────────────────────
# Python lists are flexible — one list can hold many data types together
# int, str, bool, None — all allowed in the same list

mixed = [1, 'a', True, None]      # 🎨 int + str + bool + NoneType together
print(mixed)                       # Output: [1, 'a', True, None]
print(type(mixed))                 # Output: <class 'list'>

# ──────────────────────────────────────────────────────────
# 1.5  Creating a List from String & range()
# ──────────────────────────────────────────────────────────
# list() is a constructor — it converts other iterables into a list

letters = list('Python')           # 🔄 Each character becomes a separate list item
print(letters)                     # Output: ['P', 'y', 't', 'h', 'o', 'n']

numbers = list(range(5))           # 🔄 range(5) = 0,1,2,3,4 → converted to a list
print(numbers)                     # Output: [0, 1, 2, 3, 4]

# ──────────────────────────────────────────────────────────
# 1.6  Nested List / Matrix
# ──────────────────────────────────────────────────────────
# A matrix is a list of lists — think of it like rows in a table
# Outer list = rows | Inner list = columns

matrix = [['a', 'b', 'c'],         # 🧱 Row 0
          ['d', 'e', 'f']]         # 🧱 Row 1
print(matrix)                      # Output: [['a', 'b', 'c'], ['d', 'e', 'f']]
print(type(matrix))                # Output: <class 'list'>

mixed_matrix = [['a', 'b', 'c'],   # 🎭 Row 0 — strings
                [1, 2, 3],         # 🎭 Row 1 — integers
                [True]]            # 🎭 Row 2 — boolean (each row can differ!)
print(mixed_matrix)
print(type(mixed_matrix))


# ╔══════════════════════════════════════════════════════════╗
# ║  🔍  SECTION 2 — INDEXING & SLICING                     ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# 2.1  Positive & Negative Indexing
# ──────────────────────────────────────────────────────────
# Positive index → counts from the LEFT  starting at 0
# Negative index → counts from the RIGHT starting at -1
#
#  List :  ['A',  'B',  'C',  'D']
#  +ve  :    0     1     2     3
#  -ve  :   -4    -3    -2    -1

lst = ['A', 'B', 'C', 'D']

print(lst)                         # Full list
print(len(lst))                    # 📏 Total items → 4

print(lst[0])                      # 👈 First item  → 'A'
print(lst[-1])                     # 👉 Last item   → 'D'  (negative index counts from end)
print(lst[3])                      # 👉 4th item    → 'D'

# ──────────────────────────────────────────────────────────
# 2.2  Indexing Inside a Matrix
# ──────────────────────────────────────────────────────────
# Syntax: matrix[row][column]
# 🗺️ First bracket = which row | Second bracket = which column

matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]
print(matrix)
print(matrix[2])            # 📍 Entire Row 2     → ['g', 'h', 'i']   same as matrix[-1]
print(matrix[-1][2])        # 📍 Last row, last item → 'i'            same as matrix[-1][-1]
print(matrix[0][0])         # 📍 First row, first item → 'a'
print(matrix[1][1])         # 📍 Middle item → 'e'                    same as matrix[-2][-2]

# ──────────────────────────────────────────────────────────
# 2.3  Slicing — Retrieving Multiple Items
# ──────────────────────────────────────────────────────────
# Syntax: list[start : stop]
# ✂️ The START index IS included
# ✂️ The STOP  index is NOT included (stop - 1 is the last item returned)

lst = ['a', 'b', 'c', 'd']

print(lst[:2])   # ✂️ Index 0 & 1 only  → ['a', 'b']  (stops BEFORE index 2)
print(lst[2:])   # ✂️ From index 2 to end → ['c', 'd']
print(lst[:])    # 📋 Full copy of list → ['a', 'b', 'c', 'd']


# ╔══════════════════════════════════════════════════════════╗
# ║  📦  SECTION 3 — UNPACKING LISTS                        ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# 3.1  Basic Unpacking
# ──────────────────────────────────────────────────────────
# Unpacking = assigning each list item to its own variable in one line
# Much cleaner than accessing by index one-by-one

person = ['Akash', 29, 'Data Analyst', 'Spain']

# ❌ Old way — repetitive index access:
# name    = person[0]
# age     = person[1]
# role    = person[2]
# country = person[3]

# ✅ Clean way — unpacking (one line, all variables assigned):
name, age, role, country = person
print(role)                        # Output: Data Analyst

# ──────────────────────────────────────────────────────────
# 3.2  Rest Collector — Asterisk *
# ──────────────────────────────────────────────────────────
# ⭐ The * (star) operator collects multiple leftover values into a new list
# It "vacuums up" everything that doesn't fit into named variables
# Can be placed at start, middle, or end — but only ONE * allowed per unpack

person = ['Akash', 29, 'Data Analyst', 'India']

# * in the MIDDLE — collects everything between first and last named variable
name, *details, country = person
print(name)       # Output: Akash
print(details)    # Output: [29, 'Data Analyst']   ← list of everything in between
print(country)    # Output: India

# ---------------------------------
person = [1, 'Akash', 29, 'Data Analyst', 'India']
name, *details, country = person
print(name)       # Output: 1
print(details)    # Output: ['Akash', 29, 'Data Analyst']
print(country)    # Output: India

# ---------------------------------
# * at the END — collects all remaining items after the first named variable
person = ['Akash', 29, 'Data Analyst', 'India']
name, *details = person
print(name)       # Output: Akash
print(details)    # Output: [29, 'Data Analyst', 'India']

# ---------------------------------
# * at the START — collects all leading items before the last named variable
person = ['Akash', 29, 'Data Analyst', 'India']
*details, country = person
print(details)    # Output: ['Akash', 29, 'Data Analyst']
print(country)    # Output: India

# ──────────────────────────────────────────────────────────
# 3.3  Unpacking Rules
# ──────────────────────────────────────────────────────────

# ── RULE 1: Exact Match ⚖️ ─────────────────────────────────
# Without *, the number of variables MUST exactly match the number of values.
# Too many or too few variables → ValueError

numbers = [1, 2, 3, 4]

# ❌ This would raise: ValueError: too many values to unpack
# first, second, third, fourth, last = numbers

# ── RULE 2: Asterisk (*) Catch-All 🪣 ─────────────────────
# * collects "leftovers" into a list — even if there are none (returns [])
numbers = [1]

first, *rest = numbers
print(first)   # Output: 1
print(rest)    # Output: []   ← empty list, nothing was left over

# 💡 PRO TIP: * can go anywhere in the unpack
# first, *middle, last = [1, 2, 3, 4, 5]
# middle would be [2, 3, 4]

# ──────────────────────────────────────────────────────────
# 3.4  Underscore Operator _ (Ignore Values)
# ──────────────────────────────────────────────────────────
# 🗑️ _ is a throwaway variable — use it for values you don't care about
# It's a Python convention meaning "I'm intentionally ignoring this"

person = ['Akash', 29, 'Data Analyst', 'India']

# Ignore age and role — only keep name and country
name, _, _, country = person       # Each _ discards one value
print(name)       # Output: Akash
print(country)    # Output: India

# ---------------------------------
person = ['Akash', 29, 'Data Analyst', 'India']

# *_ discards EVERYTHING in between name and country
name, *_, country = person         # 🗑️ 29 and 'Data Analyst' are silently discarded
print(name)       # Output: Akash
print(country)    # Output: India


# ╔══════════════════════════════════════════════════════════╗
# ║  🔬  SECTION 4 — EXPLORE & ANALYZE                      ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# QUICK REFERENCE TABLE
# ──────────────────────────────────────────────────────────
# max(lst)        → 🔺 Highest value
# min(lst)        → 🔻 Lowest value
# sum(lst)        → ➕ Total of all values
# len(lst)        → 📏 Number of items
# all(lst)        → ✅ True ONLY if every item is truthy
# any(lst)        → 🔍 True if AT LEAST one item is truthy
# lst.count(x)    → 🔢 How many times x appears
# lst.index(x)    → 📍 Position of FIRST occurrence of x
# x in lst        → 🪪 True if x exists in list
# x not in lst    → 🪪 True if x does NOT exist in list
# lst1 == lst2    → ⚖️ True if both lists have same VALUES
# lst1 is lst2    → 🧠 True if both point to same OBJECT in memory
# lst1 < lst2     → 📐 Compares element by element, left to right

numbers = [1, 5, 5, 4, 3]

# ──────────────────────────────────────────────────────────
# 4.1  Numeric Aggregations
# ──────────────────────────────────────────────────────────

print("Max    : ", max(numbers))      # 🔺 Highest value → 5
print("Min    : ", min(numbers))      # 🔻 Lowest value  → 1
print("Sum    : ", sum(numbers))      # ➕ Total          → 18
print("Length : ", len(numbers))      # 📏 Count          → 5

# ──────────────────────────────────────────────────────────
# 4.2  Completeness & Existence Check — all() / any()
# ──────────────────────────────────────────────────────────
# Truthy values: any non-zero number, non-empty string, True, etc.
# Falsy values : 0, '' (empty string), None, False, [] (empty list)

# all() → Returns True ONLY IF every single item is truthy
#         Even ONE falsy item returns False
print("All : ", all([numbers]))          # ✅ True  — numbers list itself is truthy
print("All : ", all([1, 0, 2]))          # ❌ False — 0 is falsy
print("All : ", all(['a', 'b', 'c']))    # ✅ True  — all non-empty strings
print("All : ", all(['a', '', 'c']))     # ❌ False — '' (empty string) is falsy

# any() → Returns True IF AT LEAST ONE item is truthy
#         Returns False only if ALL items are falsy
print("Any : ", any([numbers]))          # ✅ True  — numbers list is truthy
print("Any : ", any([1, 0, 2]))          # ✅ True  — 1 and 2 are truthy
print("Any : ", any(['a', 'b', 'c']))    # ✅ True
print("Any : ", any(['a', '', 'c']))     # ✅ True  — 'a' and 'c' are truthy

# ──────────────────────────────────────────────────────────
# 4.3  Search & Count
# ──────────────────────────────────────────────────────────
# .count(x) → counts ALL occurrences of x
# .index(x) → returns position of FIRST occurrence only
#              ⚠️ Raises ValueError if x is not in the list

print("Count : ", numbers.count(5))     # 🔢 5 appears 2 times  → 2
print("Index : ", numbers.index(5))     # 📍 First occurrence at index → 1

# ──────────────────────────────────────────────────────────
# 4.4  Membership — in / not in
# ──────────────────────────────────────────────────────────
# 'in' checks if a value EXISTS anywhere in the list
# Returns True or False

print(4 in numbers)       # ✅ True  — 4 is in the list
print(8 in numbers)       # ❌ False — 8 is not in the list

print(4 not in numbers)   # ❌ False — because 4 IS in the list
print(8 not in numbers)   # ✅ True  — because 8 is NOT in the list

# ──────────────────────────────────────────────────────────
# 4.5  Equality vs Identity — == vs is
# ──────────────────────────────────────────────────────────
# == checks if VALUES are the same (content comparison)
# is checks if they are the SAME OBJECT in memory (identity check)
# Two lists with identical values are equal (==) but NOT identical (is)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)    # ✅ True  — same values
print(list1 is list2)    # ❌ False — different objects stored at different memory addresses

list3 = [1, 2, 3, 4]
list4 = [1, 2, 3]
print(list3 == list4)    # ❌ False — different lengths, so not equal

# ──────────────────────────────────────────────────────────
# 4.6  Comparison — element-by-element
# ──────────────────────────────────────────────────────────
# Python compares lists left to right, item by item
# Stops as soon as it finds a difference and decides based on that pair

list5 = [1, 2, 3]
list6 = [5, 2, 3]
print(list5 < list6)     # ✅ True  — 1 < 5 at index 0, so list5 is "smaller"


# ╔══════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 5 — CHANGING LISTS (Add / Remove / Update) ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# 5.1  Adding Items
# ──────────────────────────────────────────────────────────
# .append(value)    → Adds ONE item to the END of the list
# .insert(i, value) → Inserts ONE item at a SPECIFIC index
#                     All items from that index onward shift RIGHT by one

letters = ['a', 'b', 'c', 'd']

letters.append('x')                # ➕ End of list → ['a','b','c','d','x']
letters.append('y')                # ➕ End of list → ['a','b','c','d','x','y']

letters.insert(1, 'f')             # 📌 At index 1 → ['a','f','b','c','d','x','y']
letters.insert(3, 'g')             # 📌 At index 3 → ['a','f','b','g','c','d','x','y']

print(letters)

# Adding to a Matrix (nested list)
matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix.append(['x', 'y', 'z'])         # ➕ Adds a new row at the END
matrix.insert(0, ['k', 'l', 'm'])      # 📌 Inserts new row at TOP (index 0)
matrix.append(['End_List'])            # ➕ Single-item row at the end

matrix[1].append('x')                  # ➕ Adds 'x' to the end of Row 1
matrix[0].insert(3, 'Z')               # 📌 Inserts 'Z' at index 3 of Row 0
matrix[1].insert(2, 'E')               # 📌 Inserts 'E' at index 2 of Row 1

print(matrix)

# ──────────────────────────────────────────────────────────
# 5.2  Removing Items
# ──────────────────────────────────────────────────────────
# .clear()          → 🗑️ Empties the ENTIRE list (keeps the list object itself)
# .remove(value)    → 🎯 Removes by VALUE — only removes the FIRST match found
#                       ⚠️ Raises ValueError if value is not in the list
# .pop(index)       → 📤 Removes AND RETURNS the item at given index
#                       Default (no index given) removes & returns the LAST item

letters = ['a', 'b', 'c', 'd', 'a']

letters.remove('a')    # 🎯 Removes FIRST 'a' (at index 0) → ['b','c','d','a']
letters.remove('a')    # 🎯 Removes next 'a' (now at last) → ['b','c','d']
print(letters)

# ──────────────────────────────────────────────────────────
letters2 = ['a', 'b', 'c', 'd', 'a']
letters2.clear()       # 🗑️ Removes all items, list becomes empty []
print(letters2)        # Output: []

# ──────────────────────────────────────────────────────────
letters3 = ['a', 'b', 'c', 'd', 'a']

removed  = letters3.pop(2)     # 📤 Removes index 2 ('c') and returns it
removed2 = letters3.pop()      # 📤 No index → removes & returns last item ('a')
print(letters3)                # Remaining: ['a', 'b', 'd']
print("Removed Item : ", removed)    # Output: c
print("Removed Item : ", removed2)   # Output: a

# ──────────────────────────────────────────────────────────
# Removing from a Matrix
matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix[1].pop(1)       # 📤 Removes 'e' (index 1) from Row 1
matrix[-1].pop(0)      # 📤 Removes 'g' (index 0) from last row (Row 2)
matrix[-3].pop(2)      # 📤 Removes 'c' (index 2) from first row (Row 0)
print(matrix)

# ──────────────────────────────────────────────────────────
# 5.3  Updating Items
# ──────────────────────────────────────────────────────────
# ⚠️ Always use an index to update a specific item
#    Assigning without an index REPLACES the entire variable (not just an item)

letters = ['a', 'b', 'c', 'd', 'e']

letters[0] = 'x'       # ✏️ Changes 'a' → 'x' at index 0
letters[1] = 'y'       # ✏️ Changes 'b' → 'y' at index 1

print(type(letters))   # Still <class 'list'>
print(letters)         # Output: ['x', 'y', 'c', 'd', 'e']

# ──────────────────────────────────────────────────────────
letters2 = ['a', 'b', 'c', 'd', 'e']
letters2 = 'z'         # ⚠️ This REPLACES the entire variable — now it's a string, not a list!
print(type(letters2))  # Output: <class 'str'>
print(letters2)        # Output: z

# ──────────────────────────────────────────────────────────
# Updating a Matrix
matrix = [
    ['a', 'b', 'c'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['g', 'h', 'i']   # Row 2
]

matrix[2] = ['x', 'y', 'z']    # ✏️ Replaces entire Row 2 with a new row
matrix[0][0] = '-'             # ✏️ Updates single cell → Row 0, Col 0
matrix[0][1] = '+'             # ✏️ Updates single cell → Row 0, Col 1
matrix[0][2] = '%'             # ✏️ Updates single cell → Row 0, Col 2
print(matrix)


# ╔══════════════════════════════════════════════════════════╗
# ║  🔄  SECTION 6 — SORTING                                 ║
# ╚══════════════════════════════════════════════════════════╝

# ──────────────────────────────────────────────────────────
# 6.1  .sort() — Sorts In Place
# ──────────────────────────────────────────────────────────
# ⚠️ .sort() MODIFIES the original list — it does NOT return a new one
# Default: Ascending (A→Z, low→high)
# reverse=True: Descending (Z→A, high→low)

letters = ['c', 'a', 'b']

letters.sort()                   # 🔼 Ascending  → ['a', 'b', 'c']
letters.sort(reverse=True)       # 🔽 Descending → ['c', 'b', 'a']
print(letters)

# ──────────────────────────────────────────────────────────
# Sorting a Matrix
# ──────────────────────────────────────────────────────────
# Python compares FIRST item of each inner list
# If first items are equal, it compares SECOND items, and so on

matrix = [
    ['g', 'h', 'i'],  # Row 0
    ['d', 'e', 'f'],  # Row 1
    ['a', 'b', 'c']   # Row 2
]
matrix.sort()          # Compares first item: 'a' < 'd' < 'g' → sorted by Row 0 first letter
print(matrix)          # Output: [['a','b','c'], ['d','e','f'], ['g','h','i']]

matrix2 = [
    ['g', 'h', 'i'],   # Row 0
    ['a', 'z', 'f'],   # Row 1 — first item 'a' same as Row 2
    ['a', 'b', 'c']    # Row 2 — first item 'a' same as Row 1
]
matrix2.sort()         # 'a'=='a' at first item → now compares SECOND item: 'b' < 'z'
print(matrix2)         # Output: [['a','b','c'], ['a','z','f'], ['g','h','i']]

# ──────────────────────────────────────────────────────────
# 6.2  sorted() — Returns a New Sorted List
# ──────────────────────────────────────────────────────────
# ✅ sorted() does NOT change the original list
# It creates and returns a BRAND NEW sorted copy

letters = ['c', 'a', 'b']
new_list = sorted(letters)         # Original untouched, sorted copy returned
print(new_list)                    # Output: ['a', 'b', 'c']
print(letters)                     # Still: ['c', 'a', 'b'] — unchanged

# ──────────────────────────────────────────────────────────
# 6.3  .reverse() — Flips List In Place
# ──────────────────────────────────────────────────────────
# ⚠️ .reverse() modifies the original AND returns None (not a new list)
# Wrapping in list() gives you an empty list — because list(None) fails
# Use reversed() (built-in) if you want a new reversed copy

letters = ['c', 'a', 'b']
new_list = list(letters.reverse())  # ⚠️ .reverse() returns None → list(None) → error-prone
print(f"Original List : {letters} \nReverse List : {new_list}")
# letters is now reversed in place, new_list is None ← common gotcha!

# ═══════════════════════════════════════════════════════════
#   SORTING SUMMARY
# ═══════════════════════════════════════════════════════════
# .sort()              → 🔼 Sorts list IN PLACE, ascending  (modifies original)
# .sort(reverse=True)  → 🔽 Sorts list IN PLACE, descending (modifies original)
# sorted(lst)          → 📋 Returns NEW sorted list          (original untouched)
# .reverse()           → 🔄 Flips list IN PLACE              (returns None!)
# reversed(lst)        → 📋 Returns NEW reversed iterator    (original untouched)
# ═══════════════════════════════════════════════════════════