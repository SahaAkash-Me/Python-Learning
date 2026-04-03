# ================================================
# PYTHON DATA STRUCTURES - LIST vs TUPLE
# Tutorial Code (Exactly as shown in the video)
# ================================================

# ==================== 1. LIST ====================

print("=== LIST DEMO ===")

# Creating a simple list
my_list = [10, 30, 20, 10] # 1. Ordered
print("Original List:", my_list) # 1. Ordered
print("List is Ordered → Order is preserved\n")
# 2. Allows Duplicates
my_list2 = [10, 30, 20, 10]          # added duplicate 10
print("List with Duplicate:", my_list2, '\n')

# 3. Indexed (Access by position - starts from 0)
print("Second element 'Indexed' (index 1):", my_list2[1], '\n')

# 4. Mutable - We CAN change it
my_list2[3] = 40                     # changing 20 → 40
print("After updating index 2 to 40:", my_list2)

print("-" * 50)


# ==================== 2. TUPLE ====================

print("=== TUPLE DEMO ===")

# Creating a tuple (use parentheses)
my_tuple = (10, 30, 20)
print("Original Tuple:", my_tuple,) # 1. Ordered
print("Tuple is Ordered → Order is preserved",'\n')

# 2. Allows Duplicates
my_tuple = (10, 30, 20, 10)
print("Tuple with Duplicate:", my_tuple,'\n')

# 3. Indexed (Same as list)
print("Second element (index 1):", my_tuple[1],'\n')

# 4. Immutable - We CANNOT change it
# This will raise an error:
#       my_tuple[2] = 40                  # ← Uncomment to see error
#       print("Tuple is Immutable (cannot be changed after creation)",'\n')

# Trying sorted() on a tuple
print(sorted(my_tuple))

sorted_tuple = sorted(my_tuple)      # sorted() always returns a LIST
print("Sorted version (using sorted()):", sorted_tuple)
print("Type of sorted result:", type(sorted_tuple),'\n')

print("-" * 50)

# ==================== SUMMARY ====================

print("SUMMARY:")
print("List   → Ordered | Duplicates Allowed | Indexed | Mutable (can change)")
print("Tuple  → Ordered | Duplicates Allowed | Indexed | Immutable (cannot change)")

print("\nWhen to use Tuple?")
print("→ When you want to protect data (database credentials, configuration, etc.)")


# ================================================
# PYTHON DATA STRUCTURES - SETS
# Tutorial Code (Exactly as shown in the video)
# ================================================

print("=== SETS IN PYTHON ===\n")

# ==================== 1. CREATING A SET ====================

# Sets are created using curly brackets {}
my_set = {10, 30, 20}
print("Original Set:", my_set)

# ==================== 2. CHARACTERISTICS OF SETS ====================

print("\n--- Characteristics of Sets ---")

# 1. Unordered → Order is NOT preserved
print("1. Unordered → Python changed the order:", my_set)

# 2. No Duplicates (Unique items only)
my_set = {10, 30, 20, 10}          # duplicate 10 will be removed
print("2. No Duplicates Allowed →", my_set)

#       3. Not Indexed → Cannot access by index
#       print(my_set[1])                  # ← This will give ERROR

# 4. Mutable → We CAN add/remove items
my_set.remove(20)
print("3. Removing 20 → ",my_set)
print("4. Mutable → We can change it after creation")

print("-" * 60)


# ==================== 3. SET METHODS ====================

print("\n=== SET METHODS ===\n")

numbers = {10, 20, 30, 40}
print("Original Set:", numbers)

# add() - Add single item
numbers.add(50)
print("After add(50):", numbers)

# update() - Add multiple items (list, tuple, or another set)
numbers.update([1, 2, 3])
numbers.update("HI")                # adds each character
print("After update([1,2,3] and 'HI'):", numbers)

# Shortcut for update using |=
numbers |= {100, 200}
print("After |= {100,200} (shortcut):", numbers)

# remove() vs discard()
numbers.remove(10)                  # removes 10
print("After remove(10):", numbers)

# numbers.remove(999)               # ← This will raise KeyError

numbers.discard(999)                # Safe remove - no error if not found
print("After discard(999) - safe:", numbers)

# pop() - removes random item (not recommended)
popped = numbers.pop()
print("After pop() - removed random item:", popped)
print("Current Set:", numbers)

print("-" * 60)


# ==================== 4. MATHEMATICAL SET OPERATIONS ====================

print("\n=== MATHEMATICAL SET OPERATIONS ===\n")

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Set A:", A)
print("Set B:", B)

# Union (all items from both sets)

print("\nUnion using method:", A.union(B))
print("Union (A | B):", (A | B))

# Intersection (common items / Shared Items)
print("Intersection using method:", A.intersection(B))
print("Intersection (A & B):", (A & B))

# Difference (items in A but not in B)
print("Difference using method:", A.difference(B))
print("Difference (A - B):", A - B)
print("Difference using method:", B.difference(A))
print("Difference (A - B):", B - A)

# Symmetric Difference (items in either set but not both)
print("Symmetric Difference using method:", A.symmetric_difference(B))
print("Symmetric Difference (A ^ B):", A ^ B)

print("-" * 60)

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

# ==================== 5. RELATIONSHIP CHECKS ====================

print("\n=== RELATIONSHIP CHECKS (True/False) ===\n")

A = {30, 40}
B = {10, 20, 30, 40, 50, 60}

print("A:", A)
print("B:", B)

print("\nIs A a subset of B?     →", A.issubset(B))      # All items of A are in B
print("Is B a superset of A?   →", B.issuperset(A))    # B contains all of A

print("Are A and B disjoint?   →", A.isdisjoint(B))    # No common items?

# Example of disjoint sets
C = {100, 200}
print("\nC:", C)
print("Are A and C disjoint?   →", A.isdisjoint(C))

print("-" * 60)

# ==================== SUMMARY ====================

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