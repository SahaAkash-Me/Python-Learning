# ╔══════════════════════════════════════════════════════════════════╗
# ║         🐍 PYTHON DATA STRUCTURES - COMPLETE TUTORIAL           ║
# ║    Lists • Tuples • Sets • Dictionaries  |  Beginner Guide      ║
# ╚══════════════════════════════════════════════════════════════════╝

# ════════════════════════════════════════════════════════════════════
# 📊 QUICK COMPARISON CHEATSHEET
# ════════════════════════════════════════════════════════════════════
#
#   TYPE          ORDERED     DUPLICATES        INDEXED       MUTABLE
#   ─────────────────────────────────────────────────────────────────
#   list  [ ]       ✅ Yes      ✅ Yes            ✅ Yes        ✅ Yes
#   tuple ( )       ✅ Yes      ✅ Yes            ✅ Yes        ❌ No
#   set   { }       ❌ No       ❌ No             ❌ No         ✅ Yes
#   dict  { }       ✅ Yes      ❌ Keys           ⚠️  Keyed     ✅ Yes
#                               ✅ Values
#   ─────────────────────────────────────────────────────────────────
#
#   💡 NOTES
#   ─────────────────────────────────────────────────────────────────
#   list  [ ]  → Most flexible. Use when order & duplicates both matter.
#   tuple ( )  → Like a list but LOCKED. Use for data that must never change.
#   set   { }  → No order, no duplicates. Great for math ops & removing dups.
#   dict  { }  → Key-Value pairs. Keys unique; values can repeat. Access by key.
#   ─────────────────────────────────────────────────────────────────

# ════════════════════════════════════════════════════════════════════
# 📑 INDEX  (Jump to any topic using its line number)
# ════════════════════════════════════════════════════════════════════
#
#   TOPIC                                               LINE
#   ─────────────────────────────────────────────────── ────
#   📦 SECTION 1 : LIST                                   94
#        1.1  Creating a List (Ordered)                  106
#        1.2  Duplicates in a List                       113
#        1.3  Indexing  (Access by position)             119
#        1.4  Mutability  (Changing an element)          124
#
#   📦 SECTION 2 : TUPLE                                 133
#        2.1  Creating a Tuple (Ordered)                 145
#        2.2  Duplicates in a Tuple                      151
#        2.3  Indexing  (Access by position)             156
#        2.4  Immutability  (Cannot be changed)          160
#        2.5  sorted() on a Tuple                        168
#
#   📊 SECTION 3 : LIST vs TUPLE  SUMMARY               181
#
#   🔵 SECTION 4 : SETS                                  198
#        4.1  Creating a Set                             211
#        4.2  Characteristics  (Unordered, No Dups…)    218
#        4.3  Set Methods                                245
#             add() · update() · |= · remove()
#             discard() · pop()
#
#   🔢 SECTION 5 : MATHEMATICAL SET OPERATIONS          296
#        5.1  Union            A ∪ B                     312
#        5.2  Intersection     A ∩ B                     318
#        5.3  Difference       A − B  /  B − A           324
#        5.4  Symmetric Diff   A Δ B                     333
#        5.5  Visual Venn Diagrams                       341
#
#   🔗 SECTION 6 : RELATIONSHIP CHECKS                  408
#        6.1  issubset()                                 427
#        6.2  issuperset()                               432
#        6.3  isdisjoint()                               437
#
#   📋 SECTION 7 : FINAL SUMMARY  (Sets)                451
#
#   📖 SECTION 8 : DICTIONARIES                         467
#        8.1  Basic Dictionary Creation                  481
#        8.2  Duplicate Keys  (last value wins)          487
#        8.3  Duplicate Values  (allowed)                494
#        8.4  Not Indexed → KeyError                     500
#        8.5  Access Value using KEY                     506
#        8.6  Updating a Value  (Mutable)                511
#        8.7  Real-World User Dictionary                 518
#        8.8  Safe Access with .get()                    524
#        8.9  Check if Key Exists  (in / not in)         532
#        8.10 View Objects: keys() values() items()      539
#        8.11 Looping — Old Way                          549
#        8.12 Modern Looping with .items()               557
#        8.13 Adding a New Key-Value Pair                563
#        8.14 Updating an Existing Key                   569
#        8.15 Update Multiple Values with .update()      575
#        8.16 Remove with .pop() + Default Value         581
#        8.17 Remove Last Item with .popitem()           591
#        8.18 .fromkeys() — Same Default Value           597
#        8.19 Dictionary Comprehension                   609
#        8.20 Bonus: Real-World Use Cases                624
#
# ════════════════════════════════════════════════════════════════════


# ================================================
# 📦 SECTION 1 : LIST
# ================================================
# 📖 A List is a collection that stores multiple items in a single
#    variable. Think of it like a shopping list — ordered, allows
#    repeated items, and you can cross things out (mutate).
#
#    Syntax : my_list = [item1, item2, item3]
# ================================================

print("=== LIST DEMO ===")

# ── 1.1  ORDERED ────────────────────────────────────────────────────
# 📌 Items always stay in the exact order you put them in.
#    Python remembers positions — index 0 is the first item.
my_list = [10, 30, 20, 10] # 1. Ordered
print("Original List:", my_list) # 1. Ordered
print("List is Ordered → Order is preserved\n")

# ── 1.2  DUPLICATES ALLOWED ─────────────────────────────────────────
# 📌 A List happily stores the same value more than once.
#    Here 10 appears at index 0 and index 3 — both are kept.
my_list2 = [10, 30, 20, 10]          # added duplicate 10
print("List with Duplicate:", my_list2, '\n')

# ── 1.3  INDEXED (Access by position) ───────────────────────────────
# 📌 Use square brackets [ ] with the position number (starts at 0).
#    my_list2[0]=10  my_list2[1]=30  my_list2[2]=20  my_list2[3]=10
print("Second element 'Indexed' (index 1):", my_list2[1], '\n')

# ── 1.4  MUTABLE (Values can be changed) ────────────────────────────
# 📌 Unlike Tuples, you can overwrite any element of a list.
#    Here we replace the value at index 3 (which was 10) with 40.
my_list2[3] = 40                     # changing 20 → 40
print("After updating index 2 to 40:", my_list2)

print("-" * 50)


# ================================================
# 📦 SECTION 2 : TUPLE
# ================================================
# 📖 A Tuple is like a List BUT it is IMMUTABLE — once created,
#    its values cannot be changed. Use it when the data should
#    stay constant (e.g. database credentials, GPS coordinates).
#
#    Syntax : my_tuple = (item1, item2, item3)
# ================================================

print("=== TUPLE DEMO ===")

# ── 2.1  ORDERED ────────────────────────────────────────────────────
# 📌 Just like lists, tuples preserve the order of insertion.
my_tuple = (10, 30, 20)
print("Original Tuple:", my_tuple,) # 1. Ordered
print("Tuple is Ordered → Order is preserved",'\n')

# ── 2.2  DUPLICATES ALLOWED ─────────────────────────────────────────
# 📌 Tuples also allow duplicate values — same rule as lists.
my_tuple = (10, 30, 20, 10)
print("Tuple with Duplicate:", my_tuple,'\n')

# ── 2.3  INDEXED (Access by position) ───────────────────────────────
# 📌 Indexing works the same as lists — use [ ] with position.
print("Second element (index 1):", my_tuple[1],'\n')

# ── 2.4  IMMUTABLE (Values CANNOT be changed) ───────────────────────
# 🚫 You CANNOT assign a new value to any index of a tuple.
#    Uncommenting the line below would raise a TypeError:
#    ➜  TypeError: 'tuple' object does not support item assignment
# This will raise an error:
#       my_tuple[2] = 40                  # ← Uncomment to see error
#       print("Tuple is Immutable (cannot be changed after creation)",'\n')

# ── 2.5  sorted() ON A TUPLE ────────────────────────────────────────
# 📌 sorted() works on tuples BUT it always RETURNS A LIST, not
#    a tuple. It does not modify the original tuple (immutable).
#    Original tuple stays the same; you get a new sorted list back.
print(sorted(my_tuple))

sorted_tuple = sorted(my_tuple)      # sorted() always returns a LIST
print("Sorted version (using sorted()):", sorted_tuple)
print("Type of sorted result:", type(sorted_tuple),'\n')

print("-" * 50)


# ================================================
# 📊 SECTION 3 : LIST vs TUPLE  —  SUMMARY
# ================================================
# 📖 Quick comparison of the two most common sequence types.
# ================================================

print("SUMMARY:")
print("List   → Ordered | Duplicates Allowed | Indexed | Mutable (can change)")
print("Tuple  → Ordered | Duplicates Allowed | Indexed | Immutable (cannot change)")

# 💡 RULE OF THUMB:
#    Use a LIST  → when data may change  (e.g. user cart, scores)
#    Use a TUPLE → when data must stay fixed (e.g. settings, coords)
print("\nWhen to use Tuple?")
print("→ When you want to protect data (database credentials, configuration, etc.)")


# ================================================
# 🔵 SECTION 4 : SETS IN PYTHON
# ================================================
# 📖 A Set is an UNORDERED collection of UNIQUE items.
#    Sets are perfect for removing duplicates and performing
#    classic math operations like union & intersection.
#
#    Syntax : my_set = {item1, item2, item3}
#    ⚠️  Empty set MUST use set() — NOT {} (that creates a dict!)
# ================================================

print("=== SETS IN PYTHON ===\n")

# ── 4.1  CREATING A SET ─────────────────────────────────────────────
# 📌 Use curly brackets { }. Python will automatically sort
#    and deduplicate the items internally.
# Sets are created using curly brackets {}
my_set = {10, 30, 20}
print("Original Set:", my_set)

# ── 4.2  CHARACTERISTICS OF SETS ────────────────────────────────────
# 📌 Four key traits that separate Sets from Lists & Tuples.

print("\n--- Characteristics of Sets ---")

# 🔀 1. UNORDERED — Python does NOT guarantee insertion order.
#       Each time you print, items may appear in a different order.
print("1. Unordered → Python changed the order:", my_set)

# 🚫 2. NO DUPLICATES — Python silently drops duplicate values.
#       Adding 10 twice still gives you only one 10 in the set.
my_set = {10, 30, 20, 10}          # duplicate 10 will be removed
print("2. No Duplicates Allowed →", my_set)

# 🚫 3. NOT INDEXED — You CANNOT use [index] to access elements.
#       Sets have no positional order, so indexing makes no sense.
#       print(my_set[1])                  # ← This will give ERROR

# ✏️  4. MUTABLE — You CAN add or remove items after creation.
#       (Individual elements are still not changeable by index.)
my_set.remove(20)
print("3. Removing 20 → ",my_set)
print("4. Mutable → We can change it after creation")

print("-" * 60)


# ================================================
# 🛠️  SECTION 4.3 : SET METHODS
# ================================================
# 📖 Python provides several built-in methods to manipulate sets.
#    Below are the most commonly used ones.
# ================================================

print("\n=== SET METHODS ===\n")

numbers = {10, 20, 30, 40}
print("Original Set:", numbers)

# ➕ add() — Adds ONE item to the set.
#    If the item already exists, the set stays unchanged.
numbers.add(50)
print("After add(50):", numbers)

# ➕ update() — Adds MULTIPLE items at once.
#    Accepts any iterable: list, tuple, another set, or even a string.
#    When a string is passed, each individual character is added.
numbers.update([1, 2, 3])
numbers.update("HI")                # adds each character
print("After update([1,2,3] and 'HI'):", numbers)

# ⚡ |= shortcut — Same as update(), but uses the pipe operator.
#    Merges another set into the existing one in-place.
numbers |= {100, 200}
print("After |= {100,200} (shortcut):", numbers)

# ❌ remove() — Removes a specific item.
#    ⚠️  Raises KeyError if the item does NOT exist in the set.
numbers.remove(10)                  # removes 10
print("After remove(10):", numbers)

# numbers.remove(999)               # ← This will raise KeyError

# ✅ discard() — Also removes a specific item.
#    ✔️  SAFE version: does NOT raise an error if item is missing.
numbers.discard(999)                # Safe remove - no error if not found
print("After discard(999) - safe:", numbers)

# 🎲 pop() — Removes and RETURNS a random item.
#    ⚠️  Not recommended when you need predictable behavior,
#       because sets are unordered — you don't know what gets removed.
popped = numbers.pop()
print("After pop() - removed random item:", popped)
print("Current Set:", numbers)

print("-" * 60)


# ================================================
# 🔢 SECTION 5 : MATHEMATICAL SET OPERATIONS
# ================================================
# 📖 Sets in Python mirror mathematical Set Theory.
#    Each operation can be done with a method OR an operator.
#    Both give the same result — choose what feels readable.
# ================================================

print("\n=== MATHEMATICAL SET OPERATIONS ===\n")

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Set A:", A)
print("Set B:", B)

# ── 5.1  UNION  (A ∪ B) ─────────────────────────────────────────────
# 📌 ALL unique elements from BOTH sets combined.
#    Think: "everything in A + everything in B, no repeats"
print("\nUnion using method:", A.union(B))
print("Union (A | B):", (A | B))

# ── 5.2  INTERSECTION  (A ∩ B) ──────────────────────────────────────
# 📌 Only elements that are COMMON to BOTH sets.
#    Think: "what do A and B share?"  →  {30, 40}
print("Intersection using method:", A.intersection(B))
print("Intersection (A & B):", (A & B))

# ── 5.3  DIFFERENCE  (A − B  and  B − A) ────────────────────────────
# 📌 A - B → elements in A that are NOT in B  →  {10, 20}
#    B - A → elements in B that are NOT in A  →  {50, 60}
#    Note: A-B and B-A give DIFFERENT results — order matters!
print("Difference using method:", A.difference(B))
print("Difference (A - B):", A - B)
print("Difference using method:", B.difference(A))
print("Difference (A - B):", B - A)

# ── 5.4  SYMMETRIC DIFFERENCE  (A Δ B) ──────────────────────────────
# 📌 Elements in EITHER set but NOT in BOTH (the non-overlapping parts).
#    Think: "everything except what they share"  →  {10, 20, 50, 60}
print("Symmetric Difference using method:", A.symmetric_difference(B))
print("Symmetric Difference (A ^ B):", A ^ B)

print("-" * 60)

# ── 5.5  VISUAL VENN DIAGRAMS ───────────────────────────────────────

# ================== UNION (A ∪ B) ==================
# All unique elements from both sets
#
#        _________       _________
#       /         \_____/         \
#      /    A      _____    B      \
#     /           /     \           \
#     \           \_____/           /
#      \_________/     \___________/
#
# Everything inside both circles


# ================== INTERSECTION (A ∩ B) ==================
# Only shared elements
#
#        _________       _________
#       /         \_____/         \
#      /    A      _____    B      \
#     /           /#####\          \
#     \           \#####/          /
#      \_________/_____\__________/
#
# ##### = common region


# ================== DIFFERENCE (A - B) ==================
# Elements in A but not in B
#
#        _________       _________
#       /         \_____/         \
#      /   #####   _____    B      \
#     /   #####   /     \          \
#     \   #####   \_____/          /
#      \_________/     \__________/
#
# ##### = only in A


# ================== DIFFERENCE (B - A) ==================
# Elements in B but not in A
#
#        _________       _________
#       /         \_____/         \
#      /    A      _____   #####   \
#     /           /     \  #####   \
#     \           \_____/  #####   /
#      \_________/     \__________/
#
# ##### = only in B


# ================== SYMMETRIC DIFFERENCE (A Δ B) ==================
# Elements in A or B but NOT both
#
#        _________       _________
#       /         \_____/         \
#      /   #####   _____   #####   \
#     /   #####   /     \  #####   \
#     \   #####   \_____/  #####   /
#      \_________/     \__________/
#
# ##### = non-overlapping parts


# ================================================
# 🔗 SECTION 6 : RELATIONSHIP CHECKS
# ================================================
# 📖 These methods check HOW two sets relate to each other.
#    They all return True or False (Boolean).
#
#    issubset()   → Is every element of A found inside B?
#    issuperset() → Does B contain all elements of A?
#    isdisjoint() → Do A and B share NO common elements at all?
# ================================================

print("\n=== RELATIONSHIP CHECKS (True/False) ===\n")

A = {30, 40}
B = {10, 20, 30, 40, 50, 60}

print("A:", A)
print("B:", B)

# ── 6.1  issubset() ─────────────────────────────────────────────────
# 📌 Returns True if ALL elements of A exist in B.
#    A = {30,40}  →  both 30 and 40 are inside B  →  True
print("\nIs A a subset of B?     →", A.issubset(B))      # All items of A are in B

# ── 6.2  issuperset() ───────────────────────────────────────────────
# 📌 The reverse of issubset(). Returns True if B contains
#    every element of A. Essentially B "wraps around" A.
print("Is B a superset of A?   →", B.issuperset(A))    # B contains all of A

# ── 6.3  isdisjoint() ───────────────────────────────────────────────
# 📌 Returns True if the two sets have NO elements in common.
#    A={30,40} and B={10,20,30…} share 30 & 40  →  False
print("Are A and B disjoint?   →", A.isdisjoint(B))    # No common items?

# Example of disjoint sets
C = {100, 200}
print("\nC:", C)
# 📌 A={30,40} and C={100,200} share nothing  →  True ✅
print("Are A and C disjoint?   →", A.isdisjoint(C))

print("-" * 60)


# ================================================
# 📋 SECTION 7 : FINAL SUMMARY  —  SETS
# ================================================

print("\n=== SUMMARY - SET CHARACTERISTICS ===")
print("• Unordered          → Order is NOT guaranteed")
print("• Unique items       → No duplicates allowed")
print("• Not Indexed        → Cannot access with [index]")
print("• Mutable            → Can add/remove items")
print("\nBest used for:")
print("   - Removing duplicates")
print("   - Fast membership testing")
print("   - Mathematical set operations")
print("   - Comparing datasets (union, intersection, etc.)")


# ================================================
# 📖 SECTION 8 : DICTIONARIES
# ================================================
# 📖 A Dictionary stores data as KEY : VALUE pairs.
#    Think of it like a real dictionary — you look up a word (key)
#    to get its meaning (value). Keys must be unique; values can repeat.
#
#    Syntax : my_dict = {'key1': value1, 'key2': value2}
#
#    ✅ Ordered (Python 3.7+)  |  ✅ Mutable  |  ❌ No duplicate keys
# ================================================

print("\n=== DICTIONARY DEMO ===\n")

# ── 8.1  BASIC DICTIONARY CREATION ──────────────────────────────────
# 📌 Use curly brackets with key-value pairs separated by colons.
#    Keys are usually strings; values can be any data type.
my_dict = {'A': 10, 'B': 20, 'C': 30}
print(my_dict)

# ── 8.2  DUPLICATE KEYS  (last value wins) ──────────────────────────
# 📌 Dictionary keys MUST be unique. If you repeat a key,
#    Python silently keeps only the LAST assigned value.
#    Here 'A' appears twice → only 'A': 40 is kept.
my_dict = {'A': 10, 'B': 20, 'C': 30, 'A': 40}
print(my_dict)        # Only one 'A' remains with value 40

# ── 8.3  DUPLICATE VALUES  (allowed) ────────────────────────────────
# 📌 While keys must be unique, VALUES can repeat freely.
#    Here both 'B' and 'D' share the value 20 — perfectly valid.
my_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 20}
print(my_dict)

# ── 8.4  NOT INDEXED  (cannot use number index) ─────────────────────
# 🚫 Dictionaries do NOT support numeric indexing like lists.
#    Trying my_dict[1] looks for KEY 1, not position 1 → KeyError.
my_dict = {'A': 10, 'B': 20, 'C': 30}
# print(my_dict[1])   # This will raise KeyError

# ── 8.5  ACCESS VALUE USING KEY  (correct way) ──────────────────────
# 📌 Always access values by their KEY, not by position.
#    my_dict['B'] → looks up key 'B' → returns 20.
print(my_dict['B'])   # Output: 20

# ── 8.6  UPDATING A VALUE  (Mutable) ────────────────────────────────
# 📌 Dictionaries are MUTABLE — you can change any value
#    by assigning a new value to an existing key.
#    Here 'C': 30 becomes 'C': 80.
my_dict['C'] = 80
print(my_dict)

# ── 8.7  REAL-WORLD USER DICTIONARY EXAMPLE ─────────────────────────
# 📌 A common real-world use: storing user profile data.
#    Each field name is the key; the user's info is the value.
user = {'id': 1, 'age': 30, 'city': 'Kolkata'}
print(user)

# ── 8.8  SAFE ACCESS WITH .get() ────────────────────────────────────
# 📌 .get() retrieves a value by key WITHOUT raising an error
#    if the key doesn't exist. It returns None (or a default you set).
#    Safer than dict[key] when the key may or may not be present.
print(user.get('city'))                    # Berlin
print(user.get('name'))                    # None
print(user.get('name', 'Unknown'))         # Unknown (default value)

# ── 8.9  CHECK IF KEY EXISTS  (in / not in) ─────────────────────────
# 📌 Use the 'in' keyword to check membership by key.
#    Returns True / False — great for conditional logic.
print('age' in user)       # True
print('name' in user)      # False
print('name' not in user)  # True

# ── 8.10  VIEW OBJECTS: keys() values() items() ─────────────────────
# 📌 These three methods give you a live "view" of the dictionary.
#    keys()   → all keys         (dict_keys object)
#    values() → all values       (dict_values object)
#    items()  → all key-value pairs as tuples  (dict_items object)
#    They update automatically if the dict changes — not a snapshot.
print(user.keys())    # dict_keys(['id', 'age', 'city'])
print(user.values())  # dict_values([1, 30, 'Berlin'])
print(user.items())   # dict_items([('id', 1), ('age', 30), ('city', 'Berlin')])

# ── 8.11  LOOPING — OLD WAY ─────────────────────────────────────────
# 📌 Looping directly over a dict gives you only the KEYS.
#    To get the value, you must index back: user[item].
#    This works, but 8.12 below is the modern preferred approach.
for item in user:
    print(item)                    # only keys
    print(item, user[item])        # key and value

# ── 8.12  MODERN LOOPING WITH .items() ──────────────────────────────
# 📌 .items() unpacks each pair into (key, value) on every iteration.
#    Cleaner, more readable, and the recommended Pythonic style.
for key, value in user.items():
    print(key, value)

# ── 8.13  ADDING A NEW KEY-VALUE PAIR ───────────────────────────────
# 📌 Simply assign to a key that doesn't exist yet.
#    Python creates the new pair automatically — no special method needed.
user['name'] = 'Akash'
print(user)

# ── 8.14  UPDATING AN EXISTING KEY ──────────────────────────────────
# 📌 Same syntax as adding — if the key already exists,
#    the value is overwritten with the new one.
user['age'] = 35
print(user)

# ── 8.15  UPDATE MULTIPLE VALUES WITH .update() ─────────────────────
# 📌 .update() lets you change several keys at once by passing
#    another dictionary. Existing keys get updated; new keys get added.
user.update({'age': 40, 'city': 'Kolkata'})
print(user)

# ── 8.16  REMOVE WITH .pop() + DEFAULT VALUE ────────────────────────
# 📌 .pop(key) removes the key and RETURNS its value.
#    If the key doesn't exist, it raises KeyError —
#    unless you provide a default (second argument), which is returned safely.
removed = user.pop('age')
print('Removed value:', removed)

# Safe pop when key doesn't exist
print(user.pop('salary', 'Not found'))

# ── 8.17  REMOVE LAST ITEM WITH .popitem() ──────────────────────────
# 📌 .popitem() removes and returns the LAST inserted key-value pair
#    as a tuple. Useful when you need LIFO (Last In, First Out) behavior.
user.popitem()   # removes the last inserted pair
print(user)

# ── 8.18  CREATE DICTIONARY WITH SAME DEFAULT VALUE — .fromkeys() ───
# 📌 dict.fromkeys(keys, default) builds a dict from a list of keys,
#    giving every key the same starting value (often None or 0).
#    Perfect for initializing a template dictionary.
keys = ['id', 'name', 'age', 'city']
new_user = dict.fromkeys(keys, None)
print(new_user)

# Later you can update specific values
new_user['age'] = 40
print(new_user)

# ── 8.19  DICTIONARY COMPREHENSION  (The Challenge Solution) ────────
# 📌 Just like list comprehensions, dict comprehensions let you
#    build a dictionary in a single readable line.
#    Here: loop through user.items(), keep only string values,
#    and convert them to UPPERCASE — compact and Pythonic.
user = {'id': 1, 'name': 'John', 'age': 30, 'city': 'Berlin'}

user_string = {
    key: value.upper()
    for key, value in user.items()
    if isinstance(value, str)      # filter: only process string values
}

print(user_string)   # {'name': 'JOHN', 'city': 'BERLIN'}

# ── 8.20  BONUS: REAL-WORLD USE CASES ───────────────────────────────
# 📌 Dictionaries shine in many everyday programming scenarios.
#    Below are three common patterns you'll see in real projects.

# 🗺️  Mapping Example — Map status codes to human-readable labels.
#     Instead of if/elif chains, a dict makes lookups instant and clean.
status_map = {1: 'Open', 2: 'In Progress', 3: 'Done'}
print(status_map[2])   # In Progress

# 🌍 Country Abbreviation Mapping — ISO codes to full country names.
#    Perfect for converting API responses into readable output.
country_map = {'DE': 'Germany', 'FR': 'France', 'IN': 'India'}
print(country_map['DE'])

# ⚙️  Configuration / Environment Variables Style
#     Nested dictionaries (dict of dicts) are great for grouping
#     related settings — like a config file loaded into Python.
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'user': 'admin'
    },
    'api': {
        'timeout': 30,
        'retries': 3
    }
}
print(config['database']['host'])
