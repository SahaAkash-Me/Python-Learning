# ════════════════════════════════════════════════════════════════════════════════
# 🔢 PYTHON BOOLEAN VALUES - COMPREHENSIVE LEARNING GUIDE
# ════════════════════════════════════════════════════════════════════════════════
#
# This document covers boolean data type fundamentals in Python, including:
# basic boolean values, truthiness concept, built-in validation functions,
# type checking, and string comparison methods.
#
# Booleans are essential for: conditional logic, loops, data validation,
# control flow decisions, and logical operations.
#
# ════════════════════════════════════════════════════════════════════════════════
# 📑 TABLE OF CONTENTS (with line numbers for quick navigation)
# ════════════════════════════════════════════════════════════════════════════════
#
# 1️⃣  BASIC BOOLEAN VALUES                             [Lines 27-35]
# 2️⃣  bool() FUNCTION: TRUTHINESS OF VALUES            [Lines 38-48]
# 3️⃣  any() AND all() FOR FIELD VALIDATION             [Lines 51-66]
# 4️⃣  TYPE CHECKING WITH isinstance()                  [Lines 69-72]
# 5️⃣  STRING START/END CHECKS                          [Lines 75-78]
# 6️⃣  BONUS: COMPLETE BOOLEAN OPERATIONS REFERENCE     [Lines 81-150]
#
# ════════════════════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════════════════════
# 1️⃣ BASIC BOOLEAN VALUES
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Boolean is a data type that can only have two values: True or False
#
# Key facts about booleans:
#    • True and False are reserved keywords in Python
#    • They are case-sensitive (must be capitalized)
#    • Booleans are a subclass of integers (True = 1, False = 0)
#    • type(True) returns <class 'bool'>
#
# When are booleans used?
#    • Conditional statements (if, elif, else)
#    • Loop control (while, for)
#    • Logical operations (and, or, not)
#    • Function return values (especially validators)
#    • Data validation and filtering
# ════════════════════════════════════════════════════════════════════════════════

print(True)         # ➜ True (boolean literal)
print(False)        # ➜ False (boolean literal)
print(type(True))   # ➜ <class 'bool'> (confirms the data type)


# ════════════════════════════════════════════════════════════════════════════════
# 2️⃣ bool() FUNCTION: TRUTHINESS OF VALUES
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# The bool() function converts any value to its boolean equivalent (True or False).
# This concept is called "truthiness" - determining if something evaluates as True.
#
# ✅ VALUES THAT ARE TRUTHY (evaluate to True):
#    • Any non-zero number (positive or negative)
#    • Any non-empty string
#    • Any non-empty list, tuple, dict, set
#    • Objects (instances of classes)
#    • True itself
#
# ❌ VALUES THAT ARE FALSY (evaluate to False):
#    • Zero (0, 0.0, 0j)
#    • Empty sequences ("", [], (), {}, set())
#    • None (special null value)
#    • False itself
#
# Why is this important?
#    • You can use any value in an if statement without explicit bool() conversion
#    • Understanding truthiness prevents bugs in conditionals
#    • Useful for checking if variables contain data
#
# Examples of truthiness in action:
#    if 5: → True (non-zero)
#    if "": → False (empty string)
#    if []: → False (empty list)
#    if None: → False
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Truthy values - non-zero numbers
print(bool(123))     # ➜ True  (non-zero number is truthy)
print(bool(-5))      # ➜ True  (negative non-zero is also truthy)

# 🔹 Truthy values - non-empty strings
print(bool("Hi"))    # ➜ True  (non-empty string is truthy)

# 🔹 Falsy values - empty sequences
print(bool(()))      # ➜ False (empty tuple is falsy)
print(bool([]))      # ➜ False (empty list is falsy)

# 🔹 Falsy values - zero
print(bool(0))       # ➜ False (zero is falsy)

# 🔹 Falsy values - empty string
print(bool(""))      # ➜ False (empty string is falsy)

# 🔹 Falsy values - None
print(bool(None))    # ➜ False (None is always falsy)


# ════════════════════════════════════════════════════════════════════════════════
# 3️⃣ any() AND all() FOR FIELD VALIDATION
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# any() and all() are built-in functions for validating multiple conditions
# at once. They work with iterables (lists, tuples, etc.) and are based on
# the truthiness concept.
#
# any(iterable):
#    • Returns True if AT LEAST ONE element is truthy
#    • Returns False if ALL elements are falsy
#    • Short-circuits: stops checking after finding first True
#    • Use case: "Does the user have at least one way to contact?" (email OR phone OR username)
#    • Perfect for optional fields validation
#
# all(iterable):
#    • Returns True if ALL elements are truthy
#    • Returns False if AT LEAST ONE element is falsy
#    • Short-circuits: stops checking after finding first False
#    • Use case: "Are all required fields filled?" (email AND phone AND username)
#    • Perfect for required fields validation
#
# Practical example - User Registration:
#    • Use any() to allow signup if user provides email OR phone OR username
#    • Use all() to allow payment only if ALL required fields are completed
#
# Real-world analogy:
#    any() → "Do you have at least one form of payment?" (Credit card OR PayPal OR Bank)
#    all() → "Do you have all required documents?" (ID AND Passport AND Birth Certificate)
# ════════════════════════════════════════════════════════════════════════════════

# 🔹 Setup: User registration field validation example
email    = ""                    # ➤ Email is empty (falsy)
phone    = "7980444222"          # ➤ Phone is filled (truthy)
username = "Akash1234"           # ➤ Username is filled (truthy)

# 🔹 any() function - Registration allowed if AT LEAST ONE field is filled
# Scenario: User can register with email OR phone OR username
print(any([email, phone, username]))  # ➜ True
# Explanation: Even though email is empty, phone and username are filled,
#              so at least one field is complete → any() returns True

# 💡 Practical use:
# if any([email, phone, username]):
#     print("✅ User can register (has at least one contact method)")
# else:
#     print("❌ User must provide at least one contact method")

# 🔹 all() function - Registration allowed only if ALL fields are filled
# Scenario: Form is complete only if user provided email AND phone AND username
print(all([email, phone, username]))  # ➜ False
# Explanation: Email is empty, so NOT all fields are complete → all() returns False

# 💡 Practical use:
# if all([email, phone, username]):
#     print("✅ All fields complete - user profile fully set up")
# else:
#     print("❌ Some fields are missing - please fill all fields")


# ════════════════════════════════════════════════════════════════════════════════
# 4️⃣ TYPE CHECKING WITH isinstance()
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# isinstance() is the Pythonic way to check if a variable is of a specific type.
# It returns a boolean value (True or False).
#
# Syntax: isinstance(object, classinfo)
#
# Why isinstance() is better than type():
#    • More readable: isinstance(x, int) vs type(x) == int
#    • Works with inheritance (important in OOP)
#    • More Pythonic style
#    • Can check multiple types: isinstance(x, (int, float))
#
# Common type checks:
#    isinstance(x, int) → Is x an integer?
#    isinstance(x, str) → Is x a string?
#    isinstance(x, bool) → Is x a boolean?
#    isinstance(x, list) → Is x a list?
#    isinstance(x, (int, float)) → Is x a number (int or float)?
#
# Important: bool is a subclass of int, so isinstance(True, int) returns True!
# ════════════════════════════════════════════════════════════════════════════════

print(isinstance(123, int))     # ➜ True (123 is an integer)
print(isinstance(True, str))    # ➜ False (True is not a string)
print(isinstance(True, int))    # ➜ True (bool is subclass of int!)


# ════════════════════════════════════════════════════════════════════════════════
# 5️⃣ STRING START/END CHECKS
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Python strings have built-in methods to check if they start or end with
# specific substrings. These methods return boolean values.
#
# String methods:
#    string.startswith(prefix) → Returns True if string starts with prefix
#    string.endswith(suffix) → Returns True if string ends with suffix
#
# These methods are case-sensitive, so be careful!
#    "Hello".startswith("hello") → False (different case)
#    "Hello".startswith("Hello") → True (same case)
#
# Use cases:
#    • Validating file extensions (.pdf, .jpg, .txt)
#    • Checking protocol in URLs (http://, https://)
#    • Email validation (ends with @gmail.com)
#    • Domain checking (example.com, example.org)
#    • Command parsing (checking command prefix)
#
# Optional parameters:
#    startswith(prefix, start, end) → Check within substring range
#    endswith(suffix, start, end) → Check within substring range
# ════════════════════════════════════════════════════════════════════════════════

print("Hello".endswith("o"))    # ➜ True ("Hello" ends with "o")
print("Hello".startswith("o"))  # ➜ False ("Hello" starts with "H", not "o")

# 🔹 More practical examples
print("Hello".startswith("He")) # ➜ True ("Hello" starts with "He")
print("Hello".endswith("lo"))   # ➜ True ("Hello" ends with "lo")

# 🔹 Case sensitivity matters!
print("Hello".startswith("h"))  # ➜ False (lowercase "h" vs uppercase "H")
print("Hello".startswith("H"))  # ➜ True (matching case)


# ════════════════════════════════════════════════════════════════════════════════
# 6️⃣ BONUS: COMPLETE BOOLEAN OPERATIONS REFERENCE
# ════════════════════════════════════════════════════════════════════════════════
# 📌 EXPLANATION:
# Here's a comprehensive reference for boolean operations and logical operators.
# These are fundamental for writing conditional logic.
#
# LOGICAL OPERATORS:
#    and → Returns True if BOTH conditions are True
#    or → Returns True if AT LEAST ONE condition is True
#    not → Returns opposite boolean value (True becomes False, vice versa)
#
# COMPARISON OPERATORS (return boolean):
#    == → Equal to
#    != → Not equal to
#    < → Less than
#    > → Greater than
#    <= → Less than or equal to
#    >= → Greater than or equal to
#
# SHORT-CIRCUIT EVALUATION:
#    • and: Stops checking if first condition is False
#    • or: Stops checking if first condition is True
#    • Saves processing time when conditions are expensive
# ════════════════════════════════════════════════════════════════════════════════

print("\n" + "="*80)
print("🔹 LOGICAL OPERATORS - and, or, not")
print("="*80)

# 🔸 and operator - both conditions must be True
print(f"True and True:   {True and True}")      # ➜ True
print(f"True and False:  {True and False}")     # ➜ False
print(f"False and False: {False and False}")    # ➜ False

# Real-world example: Login validation
username = "akash"
password = "secure123"
print(f"\n📌 Login (username AND password filled): {bool(username) and bool(password)}")

# 🔸 or operator - at least one condition must be True
print(f"\nTrue or False:   {True or False}")     # ➜ True
print(f"False or False:  {False or False}")     # ➜ False
print(f"True or True:    {True or True}")       # ➜ True

# Real-world example: Contact method
has_email = True
has_phone = False
print(f"📌 Can contact (email OR phone): {has_email or has_phone}")  # ➜ True

# 🔸 not operator - reverses boolean value
print(f"\nnot True:  {not True}")                 # ➜ False
print(f"not False: {not False}")                # ➜ True

# Real-world example: User is not admin
is_admin = False
print(f"📌 User is not admin: {not is_admin}")   # ➜ True

print("\n" + "="*80)
print("🔹 COMPARISON OPERATORS")
print("="*80)

# 🔸 Equality comparison
print(f"5 == 5:    {5 == 5}")                   # ➜ True
print(f"5 == '5':  {5 == '5'}")                 # ➜ False (different types)
print(f"5 != 3:    {5 != 3}")                   # ➜ True

# 🔸 Numeric comparison
print(f"\n10 > 5:    {10 > 5}")                   # ➜ True
print(f"10 < 5:    {10 < 5}")                   # ➜ False
print(f"10 >= 10:  {10 >= 10}")                 # ➜ True
print(f"5 <= 10:   {5 <= 10}")                  # ➜ True

# 🔸 String comparison (lexicographic/alphabetical)
print(f"\n'apple' < 'banana': {'apple' < 'banana'}")    # ➜ True
print(f"'z' > 'a':          {'z' > 'a'}")              # ➜ True

print("\n" + "="*80)
print("🔹 COMBINING MULTIPLE CONDITIONS")
print("="*80)

# 🔸 Complex logic: Age verification
age = 25
has_id = True
print(f"Adult (age >= 18 AND has_id): {age >= 18 and has_id}")  # ➜ True

# 🔸 Complex logic: Discount eligibility
is_member = True
purchase_amount = 50
min_for_discount = 100
print(f"Eligible (member OR high purchase): {is_member or purchase_amount >= min_for_discount}")  # ➜ True

# 🔸 Complex logic: Access control
is_admin = False
is_owner = True
print(f"Can delete (admin OR owner): {is_admin or is_owner}")  # ➜ True
print(f"Cannot delete (not admin AND not owner): {not is_admin and not is_owner}")  # ➜ False

print("\n" + "="*80)
print("🔹 TRUTHINESS IN CONDITIONS")
print("="*80)

# Instead of: if len(username) > 0:
# Use:       if username:
username = "Akash"
password = ""

if username:
    print(f"✅ Username provided: {username}")  # ➜ Executes (non-empty = truthy)

if not password:
    print(f"❌ Password is empty")               # ➜ Executes (empty = falsy)

# List validation
tasks = ["task1", "task2"]
if tasks:
    print(f"✅ {len(tasks)} tasks to do")      # ➜ Executes (non-empty = truthy)

empty_list = []
if not empty_list:
    print(f"📋 No tasks")                       # ➜ Executes (empty = falsy)


# ════════════════════════════════════════════════════════════════════════════════
# 🎓 KEY TAKEAWAYS & SUMMARY
# ════════════════════════════════════════════════════════════════════════════════
#
# ✓ Boolean has only two values: True and False (case-sensitive)
# ✓ Truthiness: non-zero, non-empty values are True; zero, empty, None are False
# ✓ bool() converts any value to its boolean equivalent
# ✓ any() → True if at least one element is truthy (OR logic)
# ✓ all() → True if all elements are truthy (AND logic)
# ✓ isinstance() checks data types (preferred over type())
# ✓ startswith() and endswith() check string prefixes/suffixes
# ✓ Logical operators: and, or, not
# ✓ Comparison operators: ==, !=, <, >, <=, >=
# ✓ Use truthiness directly in conditions instead of bool() conversion
# ✓ Short-circuit evaluation makes code more efficient
#
# 🔗 NEXT TOPICS TO EXPLORE:
#    • if/elif/else statements and conditional logic
#    • while loops and for loops
#    • break and continue statements
#    • Combining multiple conditions
#    • Boolean functions (returning True/False)
#
# ════════════════════════════════════════════════════════════════════════════════
