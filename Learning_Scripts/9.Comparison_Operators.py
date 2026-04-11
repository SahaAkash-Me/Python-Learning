# ════════════════════════════════════════════════════════════════════════════════
# ⚖️ PYTHON COMPARISON OPERATORS - COMPREHENSIVE LEARNING GUIDE
# ════════════════════════════════════════════════════════════════════════════════
#
# This document covers comparison operators in Python, which are used to compare
# values and return boolean results (True or False).
#
# Comparison operators are essential for:
# • Conditional statements (if, elif, else)
# • Loop control (while, for with conditions)
# • Data validation and filtering
# • Decision-making logic
# • Range checking
#
# ════════════════════════════════════════════════════════════════════════════════
# 📑 TABLE OF CONTENTS (with line numbers for quick navigation)
# ════════════════════════════════════════════════════════════════════════════════
#
# 1️⃣  BASIC COMPARISON OPERATORS                       [Lines 27-45]
# 2️⃣  STRING COMPARISON: CASE SENSITIVITY              [Lines 48-55]
# 3️⃣  ALPHABETICAL COMPARISON                          [Lines 58-61]
# 4️⃣  COMMON MISTAKE: = VS ==                          [Lines 64-71]
# 5️⃣  ASSIGNMENT VS COMPARISON                         [Lines 74-79]
# 6️⃣  CHAINED COMPARISON (RANGE CHECK)                 [Lines 82-92]
# 7️⃣  BONUS: COMPLETE COMPARISON OPERATORS REFERENCE   [Lines 95-200]
#
# ════════════════════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════════════════════
# 1️⃣ BASIC COMPARISON OPERATORS
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Comparison operators compare two values and return a boolean (True or False).
# Python supports 6 basic comparison operators.
#
# OPERATOR GUIDE:
#    == → Equal to (checks if values are the same)
#    != → Not equal to (checks if values are different)
#    > → Greater than (left value is larger than right)
#    >= → Greater than or equal to (left value ≥ right)
#    < → Less than (left value is smaller than right)
#    <= → Less than or equal to (left value ≤ right)
#
# Key differences:
#    • == checks VALUE equality (does 5 == 5.0? → True)
#    • is checks IDENTITY (are they same object in memory?)
#    • All comparisons return a boolean type
#
# Use cases:
#    • Numeric comparisons: age >= 18, salary > 50000
#    • String comparisons: username == "admin"
#    • Boolean conditions: if score > 80: print("Pass")
# ════════════════════════════════════════════════════════════════════════════════

print(10 == 10)   # ➜ True  (10 equals 10, so condition is True)
print(10 != 10)   # ➜ False (10 does NOT not-equal 10, so condition is False)
print(7 > 3)      # ➜ True  (7 is greater than 3)
print(7 >= 3)     # ➜ True  (7 is greater than OR equal to 3)
print(3 < 7)      # ➜ True  (3 is less than 7)
print(7 <= 7)     # ➜ True  (7 is less than OR equal to 7)

# 🔹 Chained comparison (multiple comparisons in one statement)
# Python evaluates left to right: 1 < 4 AND 4 < 6
print(1 < 4 < 6)  # ➜ True  (1 < 4 is True AND 4 < 6 is True, so overall True)

# 🔹 Failed chained comparison
# Python evaluates: 5 < 4 AND 4 < 6
# Since first part (5 < 4) is False, the entire expression is False
print(5 < 4 < 6)  # ➜ False (5 is NOT less than 4, so fails immediately)


# ════════════════════════════════════════════════════════════════════════════════
# 2️⃣ STRING COMPARISON: CASE SENSITIVITY
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# String comparisons in Python are case-sensitive by default.
# This means 'a' and 'A' are considered different characters.
#
# Why is case sensitivity important?
#    • Password validation (case matters!)
#    • Username matching (exact comparison)
#    • File system operations (some OS are case-sensitive)
#    • Data integrity (exact matching required)
#
# When you need case-insensitive comparison:
#    • Use .lower() to convert both strings to lowercase
#    • Use .upper() to convert both strings to uppercase
#    • Use .casefold() for advanced Unicode case-folding
#
# Methods for case handling:
#    string.lower() → Converts to lowercase
#    string.upper() → Converts to uppercase
#    string.casefold() → Advanced case-folding for non-English
#
# Performance tip:
#    • Direct comparison (==) is faster than method-based comparisons
#    • Only use .lower() / .upper() when case-insensitivity is needed
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Case-sensitive comparison (default behavior)
print("a" == "A")                     # ➜ False (lowercase 'a' ≠ uppercase 'A')

# 🔹 Case-insensitive comparison (using .lower() method)
# Both strings are converted to lowercase before comparison
print("a".lower() == "A".lower())     # ➜ True
# Breakdown:
# "a".lower() → "a"
# "A".lower() → "a"
# "a" == "a" → True


# ════════════════════════════════════════════════════════════════════════════════
# 3️⃣ ALPHABETICAL COMPARISON
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Strings can be compared alphabetically using comparison operators.
# Python uses ASCII/Unicode values to determine order.
#
# How alphabetical comparison works:
#    • Characters are compared by their ASCII code values
#    • 'a' (code 97) < 'b' (code 98) → True
#    • 'A' (code 65) < 'a' (code 97) → True (uppercase comes before lowercase!)
#    • Comparison is lexicographic (dictionary order)
#
# ASCII ordering:
#    • Numbers come first (0-9)
#    • Uppercase letters (A-Z)
#    • Lowercase letters (a-z)
#    • Special characters
#
# Practical use cases:
#    • Sorting strings: check if "apple" < "banana"
#    • Alphabetical ordering
#    • Username validation ranges
#    • Dictionary-style comparisons
#
# Important notes:
#    • Comparison is character-by-character from left
#    • "apple" < "application" → True (common prefix, "e" < "l")
#    • Length doesn't matter for comparison, only character codes
# ════════════════════════════════════════════════════════════════════════════════

print("a" < "b")  # ➜ True — "a" (ASCII 97) comes before "b" (ASCII 98)

# 🔹 More alphabetical comparison examples
print("apple" < "banana")             # ➜ True ("a" < "b", so "apple" < "banana")
print("apple" < "apple1")             # ➜ True (shorter string < longer with same prefix)
print("z" > "a")                      # ➜ True ("z" comes after "a" alphabetically)
print("Apple" < "apple")              # ➜ True (uppercase < lowercase in ASCII)


# ════════════════════════════════════════════════════════════════════════════════
# 4️⃣ COMMON MISTAKE: = VS ==
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# One of the most common Python mistakes is using = (assignment) instead of ==
# (comparison). This causes a SyntaxError.
#
# KEY DIFFERENCE:
#    = → Assignment operator (assigns value to variable)
#    == → Comparison operator (checks if values are equal)
#
# Examples of the mistake:
#    ❌ if x = 5: → SyntaxError: cannot use = in comparisons
#    ✅ if x == 5: → Correct (checks if x equals 5)
#
#    ❌ print(x = 10) → SyntaxError
#    ✅ print(x == 10) → Correct (prints True or False)
#
# When to use each:
#    • Use = only for assignment: x = 5, name = "Akash"
#    • Use == only for comparison: if x == 5, print(x == 5)
#    • Never mix them in the same expression!
#
# How Python interprets them:
#    • = changes the variable's value
#    • == evaluates to True/False without changing anything
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 INCORRECT - This would cause SyntaxError (DO NOT UNCOMMENT)
# print("a" = "A")  # ❌ SyntaxError: cannot use = in comparisons
# Why? Python thinks you're trying to assign "A" to the string literal "a"

# 🔹 CORRECT - Using == for comparison
print("a" == "A")  # ➜ False (correct usage of comparison operator)


# ════════════════════════════════════════════════════════════════════════════════
# 5️⃣ ASSIGNMENT VS COMPARISON
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Understanding the difference between assignment and comparison is crucial
# for writing correct Python code. They serve completely different purposes.
#
# ASSIGNMENT (=):
#    • Stores/updates a value in a variable
#    • One-time operation (until reassigned)
#    • No output, just modifies state
#    • Used in variable initialization
#
# COMPARISON (==):
#    • Checks if two values are equal
#    • Returns True or False
#    • Doesn't modify variables
#    • Used in conditionals and logical operations
#
# Pattern comparison:
#    x = 5      ← Assignment (store 5 in x)
#    if x == 5: ← Comparison (check if x equals 5)
#
# In memory:
#    After x = 5:     x holds the value 5
#    After x == 5:    x still holds 5, expression returns True
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Assignment - store value in variable
x = "a"            # ➤ Assign string "a" to variable x
# Now x holds the value "a"

# 🔹 Comparison - check if value matches
print(x == "a")    # ➜ True (compare: does x equal "a"?)
# x still holds "a", comparison returns True
# The variable x is NOT changed by the comparison


# ════════════════════════════════════════════════════════════════════════════════
# 6️⃣ CHAINED COMPARISON (RANGE CHECK)
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Chained comparisons allow you to check if a value falls within a range.
# Instead of: (age >= 18) and (age <= 30)
# Write: 18 <= age <= 30
#
# How chained comparison works:
#    • Evaluated left to right
#    • All conditions must be True for overall result to be True
#    • Short-circuits: stops at first False (more efficient)
#    • More readable and Pythonic
#
# Syntax: a <= b <= c
#    This is equivalent to: (a <= b) and (b <= c)
#    NOT equivalent to: (a <= b) or (b <= c)
#
# Range checking examples:
#    1 < x < 10 → x is between 1 and 10 (exclusive)
#    0 <= x <= 100 → x is between 0 and 100 (inclusive)
#    18 <= age <= 65 → age is in working age range
#    -10 <= temp <= 30 → temperature in valid range
#
# Benefits over using 'and':
#    • More readable: 18 <= age <= 30 vs (age >= 18) and (age <= 30)
#    • Less repetition: age appears once instead of twice
#    • More Pythonic and natural
#    • Variable appears only once in expression
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Range check - age between 18 and 30 (inclusive)
age = 18
print(18 <= age <= 30)  # ➜ True (18 <= 18 is True AND 18 <= 30 is True)
# Evaluation: 18 <= 18 (True) → 18 <= 30 (True) → Result: True

# 🔹 Range check - age outside the range
age = 35
print(18 <= age <= 30)  # ➜ False (18 <= 35 is True BUT 35 <= 30 is False)
# Evaluation: 18 <= 35 (True) → 35 <= 30 (False) → Result: False (stops here)

# 🔹 More chained comparison examples
score = 85
print(0 <= score <= 100)    # ➜ True (score is valid percentage)

temperature = -5
print(-10 <= temperature <= 30)  # ➜ True (temperature in range)

# 🔹 Using in if statements
age = 25
if 18 <= age <= 65:
    print("✅ Working age person")  # ➜ Executes (25 is in range)

age = 70
if 18 <= age <= 65:
    print("✅ Working age person")  # ➜ Does not execute (70 > 65)
else:
    print("⏳ Retirement age person")  # ➜ Executes instead


# ════════════════════════════════════════════════════════════════════════════════
# 7️⃣ BONUS: COMPLETE COMPARISON OPERATORS REFERENCE
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# This comprehensive reference covers all comparison scenarios and advanced topics
# that complement your core learning.
#
# SECTIONS COVERED:
#    • All 6 comparison operators with examples
#    • Type comparison (comparing different types)
#    • Value vs Identity comparison
#    • Comparison with None
#    • Boolean expressions with comparisons
#    • Real-world validation examples
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "="*80)
print("🔹 COMPARISON OPERATORS - COMPLETE REFERENCE")
print("="*80)

# 🔸 Operator: == (Equal to)
print("\n📊 EQUAL TO (==)")
print(f"5 == 5:           {5 == 5}")              # ➜ True
print(f"5 == 5.0:         {5 == 5.0}")            # ➜ True (value equality)
print(f"'hello' == 'hello': {'hello' == 'hello'}")  # ➜ True

# 🔸 Operator: != (Not equal to)
print("\n📊 NOT EQUAL TO (!=)")
print(f"5 != 3:           {5 != 3}")              # ➜ True
print(f"'a' != 'A':       {'a' != 'A'}")          # ➜ True

# 🔸 Operator: > (Greater than)
print("\n📊 GREATER THAN (>)")
print(f"10 > 5:           {10 > 5}")              # ➜ True
print(f"5 > 10:           {5 > 10}")              # ➜ False
print(f"10 > 10:          {10 > 10}")             # ➜ False (not equal, so False)

# 🔸 Operator: >= (Greater than or equal to)
print("\n📊 GREATER THAN OR EQUAL TO (>=)")
print(f"10 >= 5:          {10 >= 5}")             # ➜ True
print(f"10 >= 10:         {10 >= 10}")            # ➜ True (equal counts!)
print(f"5 >= 10:          {5 >= 10}")             # ➜ False

# 🔸 Operator: < (Less than)
print("\n📊 LESS THAN (<)")
print(f"5 < 10:           {5 < 10}")              # ➜ True
print(f"10 < 5:           {10 < 5}")              # ➜ False
print(f"5 < 5:            {5 < 5}")               # ➜ False (equal, not less)

# 🔸 Operator: <= (Less than or equal to)
print("\n📊 LESS THAN OR EQUAL TO (<=)")
print(f"5 <= 10:          {5 <= 10}")             # ➜ True
print(f"5 <= 5:           {5 <= 5}")              # ➜ True (equal counts!)
print(f"10 <= 5:          {10 <= 5}")             # ➜ False

print("\n" + "="*80)
print("🔹 COMPARING DIFFERENT DATA TYPES")
print("="*80)

# 🔸 Integer vs Float comparison
print(f"\n5 == 5.0:         {5 == 5.0}")           # ➜ True (values equal)
print(f"5 < 5.5:          {5 < 5.5}")             # ➜ True (numeric comparison)

# 🔸 String vs Number comparison (always False)
print(f"\n'5' == 5:         {'5' == 5}")           # ➜ False (different types)
print(f"'5' == '5':       {'5' == '5'}")          # ➜ True (both strings)

# 🔸 Boolean as number
print(f"\nTrue == 1:        {True == 1}")          # ➜ True (bool is subclass of int)
print(f"False == 0:       {False == 0}")          # ➜ True
print(f"True > False:     {True > False}")        # ➜ True

print("\n" + "="*80)
print("🔹 COMPARING WITH None AND TRUTHINESS")
print("="*80)

# 🔸 Comparing with None (use 'is', not '==')
x = None
print(f"\nx is None:        {x is None}")          # ➜ True (correct)
print(f"x == None:        {x == None}")           # ➜ True (works but not preferred)

# 🔸 Comparing empty vs None
empty_list = []
print(f"\n[] is None:       {empty_list is None}") # ➜ False (empty list, not None)
print(f"[] == None:       {empty_list == None}")  # ➜ False

print("\n" + "="*80)
print("🔹 REAL-WORLD VALIDATION EXAMPLES")
print("="*80)

# 🔸 Age verification
age = 21
print(f"\n✅ Age check (age >= 18): {age >= 18}")

# 🔸 Score grading
score = 85
print(f"✅ Grade check:")
if score >= 90:
    print(f"  Score {score} → Grade A")
elif score >= 80:
    print(f"  Score {score} → Grade B")  # ➜ Executes
elif score >= 70:
    print(f"  Score {score} → Grade C")
else:
    print(f"  Score {score} → Grade F")

# 🔸 Password strength
password = "SecurePass123"
is_strong = len(password) >= 8
print(f"\n✅ Password strong: {is_strong}")

# 🔸 Range validation
username_length = 8
is_valid = 3 <= username_length <= 20
print(f"✅ Username length valid: {is_valid}")

# 🔸 Multi-criteria validation
age = 25
has_license = True
has_insurance = True
can_drive = age >= 18 and has_license and has_insurance
print(f"✅ Can drive: {can_drive}")

print("\n" + "="*80)
print("🔹 COMMON PATTERNS & BEST PRACTICES")
print("="*80)

# 🔸 Pattern 1: Range checking (preferred method)
score = 75
result = 50 <= score <= 100  # ➜ Preferred
# vs
# result = (score >= 50) and (score <= 100)  # ➜ Works but less elegant

# 🔸 Pattern 2: Comparing strings (case-insensitive)
username_input = "Admin"
stored_username = "admin"
# Option 1: Using .lower()
match = username_input.lower() == stored_username.lower()  # ➜ True

# 🔸 Pattern 3: Multiple conditions
x = 5
y = 10
z = 15
# Check if values are in order
in_order = x < y < z  # ➜ True (preferred)
# vs
# in_order = (x < y) and (y < z)  # ➜ Works but longer

# 🔸 Pattern 4: Avoiding common mistake
user_age = 25
# ❌ Wrong
# if user_age = 18:  # SyntaxError!
# ✅ Correct
if user_age >= 18:
    print("Adult")    # ➜ Executes
# ✅ Also correct (checking equality)
if user_age == 25:
    print("Age is 25")  # ➜ Executes


# ════════════════════════════════════════════════════════════════════════════════
# 🎓 KEY TAKEAWAYS & SUMMARY
# ════════════════════════════════════════════════════════════════════════════════
#
# ✓ == checks if VALUES are equal; != checks if they're different
# ✓ >, >=, <, <= compare numeric or alphabetical order
# ✓ String comparison is case-sensitive by default
# ✓ Use .lower() or .upper() for case-insensitive string comparison
# ✓ Chained comparisons (a <= x <= b) are more readable than (a <= x) and (x <= b)
# ✓ NEVER use = (assignment) in comparisons; always use == (comparison)
# ✓ Comparisons work with strings (alphabetical order), numbers (numeric), etc.
# ✓ True == 1 and False == 0 (booleans are integers in Python)
# ✓ Use 'is' for None comparison, not '=='
# ✓ Short-circuit evaluation: chained comparisons stop at first False
# ✓ Comparison operators return boolean True or False
#
# 🔗 NEXT TOPICS TO EXPLORE:
#    • Logical operators (and, or, not)
#    • if/elif/else conditional statements
#    • Combining comparisons in complex conditions
#    • Boolean logic and decision trees
#    • Comparison operators in loops
#    • Data filtering with comparisons
#
# ════════════════════════════════════════════════════════════════════════════════
